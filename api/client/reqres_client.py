import requests
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))
from config import APIConfig


class ReqresClient:
    def __init__(self):
        self.base_url = APIConfig.BASE_URL
        self.timeout = APIConfig.TIMEOUT
        self.headers = {
            "x-api-key": "reqres-free-v1",
            "Content-Type": "application/json"
        }

    def _send_request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}/{endpoint}"
        headers = {**self.headers, **kwargs.pop('headers', {})}
        return requests.request(
            method,
            url,
            headers=headers,
            timeout=self.timeout,
            **kwargs
        )

    def get_users(self, page=1):
        return self._send_request("GET", f"users?page={page}")

    def get_user(self, user_id):
        return self._send_request("GET", f"users/{user_id}")

    def create_user(self, data):
        return self._send_request("POST", "users", json=data)

    def update_user(self, user_id, data):
        return self._send_request("PUT", f"users/{user_id}", json=data)

    def delete_user(self, user_id):
        return self._send_request("DELETE", f"users/{user_id}")

    def login(self, credentials):
        return self._send_request("POST", "login", json=credentials)

    def register(self, data):
        return self._send_request("POST", "register", json=data)

    def get_resources(self):
        return self._send_request("GET", "unknown")

    def get_resource(self, resource_id):
        return self._send_request("GET", f"unknown/{resource_id}")

