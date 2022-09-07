"""
auth service
"""

import cattrs

from .crud import BaseService
from .models import AdminAuth, UserAuth
from .pocketbase import PocketBase


class AuthService(BaseService):
    def __init__(self, pocketbase: PocketBase):
        super().__init__(pocketbase)

    def auth_via_email(self, email: str, password: str, admin: bool) -> AdminAuth | UserAuth:
        target = "admin" if admin else "users"
        clazz = AdminAuth if admin else UserAuth
        response = self.client().http().post(url=f"{self.client().url}/api/{target}/auth-via-email",
                                             json={"email": email, "password": password})
        if response.is_success:
            json = response.json()
            self.client().auth_store.save(json["token"])
            return cattrs.structure(json, clazz)
