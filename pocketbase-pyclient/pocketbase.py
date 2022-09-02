# _*_ coding: utf-8 _*_
# @Time : 2022/9/3 2:46
# @Author : Kirovj
# @File : pocketbase.py
# @desc : client for pocketbase

import requests


class PocketBase:
    def __init__(self, url: str, authorization: str = None):
        self._api = None
        self._collection = None
        self._url = url
        self._authorization = authorization

    def login(self, email: str, password: str):
        """
        login in pocketbase with email and password
        :param email: email addr for login
        :param password: password for login
        """
        pass

    def connect(self, collection: str):
        """
        define which collection to connect and build api
        :param collection: collection you wang to connect
        """
        self._collection = collection
        self._api = self._url + f"api/collections/{self._collection}/records"

    def _check_connection(self):
        assert self._collection is not None and self._collection != ""

    @property
    def header(self):
        return {
            "Authorization": self._authorization
        }

    def list(self):
        self._check_connection()
        r = requests.get(self._api, headers=self.header)
        return r.json()

    def list_items(self):
        return self.list()["items"]

    def create(self, item: dict):
        self._check_connection()
        r = requests.post(self._api, headers=self.header, json=item)
        return r


