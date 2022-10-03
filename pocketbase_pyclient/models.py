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


class AdminModel:
    id: str = ""
    created: str = ""
    updated: str = ""
    avatar: int = 0
    email: str = ""
    last_reset_sent_at: str = ""


class AdminAuth:
    token: str = ""
    admin: AdminModel = None


class UserModel:
    id: str = ""
    created: str = ""
    updated: str = ""
    verified: bool = False
    avatar: int = 0
    email: str = ""
    last_reset_sent_at: str = ""
    last_verification_sent_at: str = ""
    # profile: {} = {}


class UserAuth:
    token: str = ""
    user: UserModel = None
    # meta: {} = {}
