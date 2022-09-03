# _*_ coding: utf-8 _*_
# @Time : 2022/9/4 2:50
# @Author : Kirovj
# @File : auth.py
# @desc :

from .pocketbase import PocketBase


class AuthService:
    def __init__(self, pocketbase: PocketBase):
        self.pocketbase = pocketbase

    def auth_via_email(self, email: str, password: str):
        response = self.pocketbase.http_client().post(url=f"{self.pocketbase.url}/api/users/auth-via-email",
                                                      json={"email": email, "password": password})
        if response.is_success:
            self.pocketbase.auth_store.save(response.json()["token"])
