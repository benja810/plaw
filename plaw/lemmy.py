from .requestor import Requestor, HttpType


class Lemmy:
    def __enter__(self):
        """Handle the context manager open."""
        return self

    def __exit__(self, *_args):
        """Handle the context manager close."""

    def __init__(self, instance, username, password):
        self.instance = instance
        self.username = username

        # Login, get token, and set as header for future
        self._req = Requestor({})
        self.auth_token = self.login(username, password)
        self._req.headers.update({"Authorization": "Bearer " + self.auth_token})
        # print(self._req.headers.get("Authorization"))

    def login(self, username, password):
        url = self.instance + "/api/v3/user/login"
        res_data = self._req.request(
            HttpType.POST, url, {"username_or_email": username, "password": password}
        )
        return res_data["jwt"]

    def getCommunity(self, name):
        url = self.instance + "/api/v3/community"
        return self._req.request(HttpType.GET, url, {"name": name})