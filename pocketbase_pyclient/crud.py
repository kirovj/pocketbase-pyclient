"""
crud service
"""
from abc import ABC

from .pocketbase import PocketBase


def _make_params(page, per_page, _sort, _filter):
    return {
        "page": page,
        "perPage": per_page,
        "sort": _sort,
        "filter": _filter
    }


class BaseService(ABC):
    def __init__(self, pocketbase: PocketBase):
        self._pocketbase = pocketbase

    def client(self):
        return self._pocketbase

    def path(self, collection: str):
        """Return service path"""


class CrudService(BaseService):
    def __init__(self, pocketbase: PocketBase):
        super(CrudService, self).__init__(pocketbase)

    def path(self, collection: str):
        return f"/api/collections/{collection}/records"

    def path_with_id(self, collection: str, _id: str):
        return f"{self.path(collection)}/{_id}"

    def list(self, collection: str, page: int = 1, per_page: int = 30, _sort: str = "", _filter: str = ""):
        return self.client().request(self.path(collection), params=_make_params(page, per_page, _sort, _filter))

    def view(self, collection, _id: str):
        return self.client().request(self.path_with_id(collection, _id))

    def create(self, collection: str, item):
        return self.client().request(self.path(collection), "POST", json=item)

    def update(self, collection: str, _id: str, item):
        return self.client().request(self.path_with_id(collection, _id), "PATCH", json=item)

    def delete(self, collection: str, _id: str):
        return self.client().request(self.path_with_id(collection, _id), "DELETE")
