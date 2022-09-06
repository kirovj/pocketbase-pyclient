# _*_ coding: utf-8 _*_
# @Time : 2022/9/3 2:46
# @Author : Kirovj
# @File : pocketbase.py
# @desc : client for pocketbase

import httpx


class PocketBase:
    def __init__(self, url: str):
        from .auth import AuthService
        from .models import AuthStore
        from .crud import CrudService
        self.url = url.strip('/')
        self.api = None
        self.collection = None
        self.auth_store: AuthStore = AuthStore()
        self._http = httpx.Client()
        self._auth_service = AuthService(self)
        self._crud_service = CrudService(self)

    def http(self):
        return self._http

    def auth_via_email(self, email: str, password: str, admin: bool = False):
        """
        login in pocketbase with email and password
        :param email: email addr for login
        :param password: password for login
        :param admin: login in as admin or not, default false
        """
        self._auth_service.auth_via_email(email, password, admin)

    def connect(self, collection: str):
        """
        define which collection to connect and build api
        :param collection: collection you wang to connect
        """
        self.collection = collection
        self.api = self.url + f"/api/collections/{self.collection}/records"

    def list(self):
        response = self._http.get(self.api, headers=self.auth_store.to_dict())
        return response.json()

    def list_items(self):
        return self.list()["items"]

    # def create(self, item: dict):
    #     r = requests.post(self._api, headers=self.header, json=item)
    #     return r
