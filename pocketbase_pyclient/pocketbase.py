"""
PocketBase client
"""


class PocketBase:
    def __init__(self, url: str):
        from .auth import AuthService
        from .models import AuthStore
        from .crud import CrudService
        self.url = url.strip('/')
        self.api = None
        self.collection = None
        self.auth_store: AuthStore = AuthStore()
        self._auth_service = AuthService(self)
        self._crud_service = CrudService(self)

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
        self._crud_service.api = self.api

    def list(self):
        return self._crud_service.list()

    def list_items(self):
        return self._crud_service.list_items()

    def create(self, item: dict):
        return self._crud_service.create(item)
