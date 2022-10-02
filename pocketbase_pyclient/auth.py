"""
auth service
"""

import httpx

from .crud import BaseService
from .models import AdminAuth, UserAuth
from .pocketbase import PocketBase


class AuthService(BaseService):
    def __init__(self, pocketbase: PocketBase):
        super().__init__(pocketbase)

    def auth_via_email(self, email: str, password: str, admin: bool) -> AdminAuth | UserAuth:
        target = "admins" if admin else "users"
        prefix = "Admin" if admin else "User"
        # clazz = AdminAuth if admin else UserAuth
        response = httpx.post(url=f"{self.client().url}/api/{target}/auth-via-email",
                              json={"email": email, "password": password})
        if response.is_success:
            json = response.json()
            self.client().auth_store.save(f"{prefix} {json['token']}")
