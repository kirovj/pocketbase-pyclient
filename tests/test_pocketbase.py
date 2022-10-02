from pocketbase_pyclient import PocketBase


class TestPocketBase:
    pb = PocketBase("http://127.0.0.1:8090/")
    pb.auth_via_email("test@kirovj.com", "testpassword", admin=True)
    pb.create("test", {
        "name": "kirovj",
        "age": 18,
        "sexual": True,
        "birthday": "2022-01-01",
        "grade": "one",
        "image": None,
    })

    def test_auth_via_email(self):
        assert self.pb.auth_store.success()

    def test_list(self):
        assert self.pb.list("test")["page"] >= 1

    def test_list_items(self):
        assert len(self.pb.list_items("test")) >= 1

    def test_view(self):
        item = self.pb.list_items("test")[0]
        assert self.pb.view("test", _id=item["id"])["name"] == "kirovj"

    def test_create(self):
        from random import randint
        item = {"name": f"kirovj{randint(0, 1000)}", "sexual": True, "grade": "two"}
        assert self.pb.create("test", item).is_success
        item["name"] = "kirovj"
        assert self.pb.create("test", item).status_code == 400

    def test_update(self):
        item = self.pb.list_items("test")[0]
        item["age"] = 99
        self.pb.update("test", item["id"], item)
        item = self.pb.list_items("test")[0]
        assert item["age"] == 99
        item["age"] = 18
        self.pb.update("test", item["id"], item)
