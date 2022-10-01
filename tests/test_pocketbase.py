from pocketbase_pyclient import PocketBase


class TestPocketBase:
    pb = PocketBase("http://127.0.0.1:8090/")
    pb.auth_via_email("test@kirovj.com", "testpassword")

    def test_auth_via_email(self):
        assert self.pb.auth_store.success()

    def test_list(self):
        assert self.pb.list("test")["page"] >= 1

    def test_list_items(self):
        assert len(self.pb.list_items("test")) >= 1

    def test_view(self):
        assert self.pb.view("test", _id="cgbi69g623hn8rk")["name"] == "jack"

    def test_create(self):
        from random import randint
        assert self.pb.create("test", {"name": f"jack{randint(0, 1000)}", "age": 18}).is_success
        assert self.pb.create("test", {"name": "jack", "age": 19}).status_code == 400
