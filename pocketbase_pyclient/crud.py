# _*_ coding: utf-8 _*_
# @Time : 2022/9/4 19:13
# @Author : Kirovj
# @File : crud.py
# @desc :
from .pocketbase import PocketBase


class BaseService:
    def __init__(self, pocketbase: PocketBase):
        self._pocketbase = pocketbase

    def client(self):
        return self._pocketbase


class CrudService(BaseService):
    pass
