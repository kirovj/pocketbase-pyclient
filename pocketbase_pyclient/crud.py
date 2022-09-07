"""
crud service
"""

from .pocketbase import PocketBase


class BaseService:
    def __init__(self, pocketbase: PocketBase):
        self._pocketbase = pocketbase

    def client(self):
        return self._pocketbase


class CrudService(BaseService):
    pass
