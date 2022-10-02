"""
PocketBase client
"""


class PocketBase:
    def __init__(self, url: str):
        from .auth import AuthService
        from .models import AuthStore
        from .crud import CrudService
        self.url = url.strip("/")
        self.auth_store: AuthStore = AuthStore()
        self._auth_service = AuthService(self)
        self.records = CrudService(self)

    def auth_via_email(self, email: str, password: str, admin: bool = False):
        """
        login in pocketbase with email and password
        :param email: email addr for login
        :param password: password for login
        :param admin: login in as admin or not, default false
        """
        self._auth_service.auth_via_email(email, password, admin)
