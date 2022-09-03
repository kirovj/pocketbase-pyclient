# _*_ coding: utf-8 _*_
# @Time : 2022/9/4 2:58
# @Author : Kirovj
# @File : models.py
# @desc :

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
