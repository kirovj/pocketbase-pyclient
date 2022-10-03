"""
PocketBase client
"""
from typing import Any

import httpx

from pocketbase_pyclient.models import AuthStore
from pocketbase_pyclient.services import AuthService, CrudService


class ClientException(Exception):
    path: str = ""
    status: int = 0
    data: dict = {}
    origin: Any | None = None

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args)
        self.path = kwargs.get("path", "")
        self.status = kwargs.get("status", 0)
        self.data = kwargs.get("data", {})
        self.origin = kwargs.get("origin", None)


def _default_request_config():
    return {
        "method": "GET",
        "headers": {},
        "params": {},
        "body": {}
    }


def _process_response(response):
    try:
        data = response.json()
    except Exception as e1:
        _ = e1
        data = None
    if response.status_code >= 400:
        raise ClientException(
            "Request fail",
            url=response.url,
            status=response.status_code,
            data=data,
        )
    return data


class PocketBase:
    def __init__(self, url: str):
        self.url = url.strip("/")
        self.auth_store: AuthStore = AuthStore()
        self._auth = AuthService(self)
        self.records = CrudService(self)
        self.httpx = httpx.AsyncClient()
        self.asyncable = True

    def auth_via_email(self, email: str, password: str, admin: bool = False):
        """
        login in pocketbase with email and password
        :param email: email addr for login
        :param password: password for login
        :param admin: login in as admin or not, default false
        """
        self._auth.auth_via_email(email, password, admin)

    def disable_async_request(self):
        """Use sync http request all the time"""
        self.asyncable = False

    def _prepare(self, request_config: dict[str: Any]):
        config = _default_request_config()
        request_config["headers"] = {}
        request_config["headers"].update(self.auth_store.to_dict())
        config.update(request_config)
        return config

    def sync_send(self, path: str, request_config: dict[str:Any]) -> Any:
        config = self._prepare(request_config)
        try:
            response = httpx.request(
                url=self.url + path,
                method=config["method"],
                headers=config["headers"],
                params=config["params"],
                json=config["body"]
            )
        except Exception as e:
            raise ClientException("Generate sync request fail", origin=e)
        return _process_response(response)

    async def async_send(self, path: str, request_config: dict[str:Any]) -> Any:
        if not self.asyncable:
            return self.sync_send(path, request_config)
        config = self._prepare(request_config)
        try:
            response = await self.httpx.request(
                url=self.url + path,
                method=config["method"],
                headers=config["headers"],
                params=config["params"],
                json=config["body"]
            )
        except Exception as e:
            raise ClientException("Generate async request fail", origin=e)
        return _process_response(response)
