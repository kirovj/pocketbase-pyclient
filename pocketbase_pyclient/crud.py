"""
crud service
"""
import httpx

from .pocketbase import PocketBase


class BaseService:
    def __init__(self, pocketbase: PocketBase):
        self._pocketbase = pocketbase

    def client(self):
        return self._pocketbase

    def auth_header(self):
        return self._pocketbase.auth_store.to_dict()

    def request(self, url, method: str = 'GET', params=None, json=None):
        return httpx.request(url=url, method=method, params=params, json=json, headers=self.auth_header())


class CrudService(BaseService):
    def __init__(self, pocketbase: PocketBase):
        super(CrudService, self).__init__(pocketbase)

    def _api(self, collection: str):
        return f"{self.client().url}/api/collections/{collection}/records"

    def list(self, collection: str):
        return self.request(self._api(collection)).json()

    def list_items(self, collection: str):
        return self.list(collection)['items']

    def create(self, collection: str, item):
        return self.request(self._api(collection), 'POST', json=item)

    def update(self, collection: str, item):
        pass
