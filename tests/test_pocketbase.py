# _*_ coding: utf-8 _*_
# @Time : 2022/9/4 4:03
# @Author : Kirovj
# @File : test_pocketbase.py
# @desc :
from pocketbase_pyclient import PocketBase


class TestPocketBase:

    pb = PocketBase("http://127.0.0.1:8090/")
    pb.auth_via_email("test@kirovj.com", "testpassword")
    pb.connect("tag")

    def test_auth_via_email(self):
        assert self.pb.auth_store.success()

    def test_list(self):
        assert self.pb.list()["page"] >= 1
