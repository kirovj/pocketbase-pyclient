"""
PocketBase client
"""
from typing import Any

import httpx


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


class PocketBase:
    def __init__(self, url: str):
        from .auth import AuthService
        from .models import AuthStore
        from .crud import CrudService
        self.url = url.strip("/")
        self.auth_store: AuthStore = AuthStore()
        self._auth = AuthService(self)
        self.records = CrudService(self)
        self.httpx = httpx.AsyncClient()

    def auth_via_email(self, email: str, password: str, admin: bool = False):
        """
        login in pocketbase with email and password
        :param email: email addr for login
        :param password: password for login
        :param admin: login in as admin or not, default false
        """
        self._auth.auth_via_email(email, password, admin)

    async def request(
            self,
            path: str,
            method: str = "GET",
            headers: dict = None,
            params: dict = None,
            json: dict = None
    ) -> Any:
        headers.update(self.auth_store.to_dict())
        try:
            response = await self.httpx.request(
                url=self.url + path,
                method=method,
                headers=headers,
                params=params,
                json=json
            )
        except Exception as e:
            raise ClientException("Build request fail", origin=e)
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
