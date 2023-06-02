from enum import Enum

import requests


class ReqresInEndpoint(str, Enum):
    list_of_users = "users"
    create_user = "register"
    list_of_resources = "unknown"
    delete_user = "users/2"


PIXEGAMI_ENDPOINT = "https://todo.pixegami.io/"


class PixegamiApiEndpoint:

    @staticmethod
    def create_task(payload) -> requests.Response:
        return requests.put(PIXEGAMI_ENDPOINT + '/create-task', json=payload)

    @staticmethod
    def update_task(payload) -> requests.Response:
        return requests.put(PIXEGAMI_ENDPOINT + f'/update-task', json=payload)

    @staticmethod
    def delete_task(task_id) -> requests.Response:
        return requests.delete(PIXEGAMI_ENDPOINT + f'/delete-task/{task_id}')

    @staticmethod
    def get_task(task_id) -> requests.Response:
        return requests.get(PIXEGAMI_ENDPOINT + f'/get-task/{task_id}')

    @staticmethod
    def list_tasks(user_id) -> requests.Response:
        return requests.get(PIXEGAMI_ENDPOINT + f'/list-tasks/{user_id}')
