# _*_ coding: utf-8 _*_
# @Time : 2022/9/4 2:50
# @Author : Kirovj
# @File : auth.py
# @desc :
from .crud import BaseService
from .pocketbase import PocketBase


class AuthService(BaseService):
    def __init__(self, pocketbase: PocketBase):
        super().__init__(pocketbase)

    def auth_via_email(self, email: str, password: str):
        response = self.client().http().post(url=f"{self.client().url}/api/users/auth-via-email",
                                             json={"email": email, "password": password})
        if response.is_success:
            self.client().auth_store.save(response.json()["token"])
