from typing import Any

import requests

from models.Enpoints import ReqresInEndpoint


class ApiClient:

    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_request(self, endpoint: ReqresInEndpoint) -> requests.Response:
        response = requests.get(
            url=self.base_url + endpoint
        )
        return response

    def post_request(self, endpoint: ReqresInEndpoint, body: Any = None) -> requests.Response:
        response = requests.post(
            url=self.base_url + endpoint,
            data=body
        )
        return response

    def delete_request(self, endpoint: ReqresInEndpoint) -> requests.Response:
        response = requests.delete(
            url=self.base_url + endpoint
        )
        return response
