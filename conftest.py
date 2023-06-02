import uuid

import pytest

from models.ApiClient import ApiClient


@pytest.fixture
def api_client() -> ApiClient:
    return ApiClient(base_url="https://reqres.in/api/")


@pytest.fixture
def new_task_payload():
    user_id = f'test_user_{uuid.uuid4().hex}'
    content = f'test_content_{uuid.uuid4().hex}'

    print(f'Creating task for user {user_id} with content {content}')

    return {
        "content": content,
        "user_id": user_id,
        "is_done": False
    }
