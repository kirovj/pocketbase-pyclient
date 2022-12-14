"""
crud service
"""
import httpx

from .pocketbase import PocketBase


def _make_params(page, per_page, _sort, _filter):
    return {
        "page": page,
        "perPage": per_page,
        "sort": _sort,
        "filter": _filter
    }


class BaseService:
    def __init__(self, pocketbase: PocketBase):
        self._pocketbase = pocketbase
        self.url = pocketbase.url

    def client(self):
        return self._pocketbase

    def auth_header(self):
        return self._pocketbase.auth_store.to_dict()

    def request(self, url, method: str = "GET", params=None, json=None):
        return httpx.request(url=url, method=method, params=params, json=json, headers=self.auth_header())


class CrudService(BaseService):
    def __init__(self, pocketbase: PocketBase):
        super(CrudService, self).__init__(pocketbase)

    def _api(self, collection: str):
        return f"{self.url}/api/collections/{collection}/records"

    def _id_api(self, collection: str, _id: str):
        return f"{self._api(collection)}/{_id}"

    def list(self, collection: str, page: int = 1, per_page: int = 30, _sort: str = "", _filter: str = ""):
        return self.request(self._api(collection), params=_make_params(page, per_page, _sort, _filter)).json()

    def list_items(self, collection: str, page: int = 1, per_page: int = 30, _sort: str = "", _filter: str = ""):
        return self.list(collection, page, per_page, _sort, _filter)["items"]

    def view(self, collection, _id: str):
        return self.request(self._id_api(collection, _id)).json()

    def create(self, collection: str, item):
        return self.request(self._api(collection), "POST", json=item)

    def update(self, collection: str, _id: str, item):
        return self.request(self._id_api(collection, _id), "PATCH", json=item)

    def delete(self, collection: str, _id: str):
        return self.request(self._id_api(collection, _id), "DELETE")
