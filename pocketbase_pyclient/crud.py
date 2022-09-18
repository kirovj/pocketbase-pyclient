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

    def list(self):
        return self.request(self.client().api).json()

    def list_items(self):
        return self.list()['items']

    def create(self, item):
        return self.request(self.client().api, 'POST', json=item)
