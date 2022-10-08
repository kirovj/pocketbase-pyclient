from abc import ABC


def _make_params(page, per_page, _sort, _filter):
    return {
        "page": page,
        "perPage": per_page,
        "sort": _sort,
        "filter": _filter
    }


class BaseService(ABC):
    def __init__(self, pocketbase):
        self.client = pocketbase

    def path(self, collection: str):
        """Return service path"""


class AuthService(BaseService):
    def __init__(self, pocketbase):
        super().__init__(pocketbase)

    def path(self, typo: str):
        return f"/api/{typo}/auth-via-email"

    def auth_via_email(self, email: str, password: str, admin: bool):
        typo = "admins" if admin else "users"
        prefix = "Admin" if admin else "User"
        response = self.client.sync_send(
            path=self.path(typo),
            request_config={
                "method": "POST",
                "body": {"email": email, "password": password}
            }
        )
        self.client.auth_store.save(f"{prefix} {response['token']}")


class CrudService(BaseService):
    def __init__(self, pocketbase):
        super(CrudService, self).__init__(pocketbase)

    def path(self, collection: str):
        return f"/api/collections/{collection}/records"

    def path_with_id(self, collection: str, _id: str):
        return f"{self.path(collection)}/{_id}"

    def list(self, collection: str, page: int = 1, per_page: int = 30, _sort: str = "", _filter: str = ""):
        return self.client.sync_send(
            self.path(collection),
            {"params": _make_params(page, per_page, _sort, _filter)}
        )

    def list_items(self, collection: str, page: int = 1, per_page: int = 30, _sort: str = "", _filter: str = ""):
        page = self.list(collection, page, per_page, _sort, _filter)
        if page["items"]:
            return page["items"]
        return []

    def view(self, collection, _id: str):
        return self.client.sync_send(self.path_with_id(collection, _id))

    def create(self, collection: str, item):
        return self.client.sync_send(
            self.path(collection),
            {"method": "POST", "body": item}
        )

    async def async_create(self, collection: str, item):
        return await self.client.async_send(
            self.path(collection),
            {"method": "POST", "body": item}
        )

    def update(self, collection: str, _id: str, item):
        return self.client.sync_send(
            self.path_with_id(collection, _id),
            {"method": "PATCH", "body": item}
        )

    def delete(self, collection: str, _id: str):
        return self.client.sync_send(self.path_with_id(collection, _id), {"method": "DELETE"})
