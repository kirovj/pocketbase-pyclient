"""
PocketBase client
"""


class PocketBase:
    def __init__(self, url: str):
        from .auth import AuthService
        from .models import AuthStore
        from .crud import CrudService
        self.url = url.strip('/')
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

    def list(self, collection: str, page: int = 1, per_page: int = 30, _sort: str = '', _filter: str = ''):
        return self._crud_service.list(collection, page=page, per_page=per_page, _sort=_sort, _filter=_filter)

    def list_items(self, collection: str, page: int = 1, per_page: int = 30, _sort: str = '', _filter: str = ''):
        return self.list(collection, page, per_page, _sort, _filter)['items']

    def create(self, collection: str, item: dict):
        return self._crud_service.create(collection, item)

    def update(self, collection: str, item: dict):
        return self._crud_service.update(collection, item)
