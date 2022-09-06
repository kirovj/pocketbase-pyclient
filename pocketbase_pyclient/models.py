# _*_ coding: utf-8 _*_
# @Time : 2022/9/4 2:58
# @Author : Kirovj
# @File : models.py
# @desc :
from attrs import define


class AuthStore:
    def __init__(self):
        self._token = ""

    def save(self, token):
        self._token = token

    def clear(self):
        self._token = ""

    def success(self):
        return self._token != ""

    def to_dict(self):
        return {
            "Authorization": self._token
        }


@define
class AdminModel:
    id: str = ""
    created: str = ""
    updated: str = ""
    avatar: int = 0
    email: str = ""
    last_reset_sent_at: str = ""


@define
class AdminAuth:
    token: str = ""
    admin: AdminModel = None


@define
class UserModel:
    id: str = ""
    created: str = ""
    updated: str = ""
    verified: bool = False
    avatar: int = 0
    email: str = ""
    last_reset_sent_at: str = ""
    last_verification_sent_at: str = ""
    # profile: {} = {}


@define
class UserAuth:
    token: str = ""
    user: UserModel = None
    # meta: {} = {}
