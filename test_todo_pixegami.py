from models.Enpoints import PixegamiApiEndpoint as api


def test_can_create_task():
    payload = {
        "content": "my_test_content",
        "user_id": "test_user",
        "is_done": False
    }
    create_task_response = api.create_task(payload)
    assert create_task_response.status_code == 200
    data = create_task_response.json()

    task_id = data['task']['task_id']
    get_task_response = api.get_task(task_id)

    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    assert get_task_data['content'] == payload['content']
    assert get_task_data['user_id'] == payload['user_id']


def test_can_update_item(new_task_payload):
    # создание задачи
    create_task_response = api.create_task(payload=new_task_payload)
    task_id = create_task_response.json()['task']['task_id']

    # обновление задачи
    new_payload = {
        "user_id": new_task_payload['user_id'],
        "task_id": task_id,
        "content": "my_updated_content",
        "is_done": True
    }
    update_task_response = api.update_task(payload=new_payload)
    assert update_task_response.status_code == 200

    # получение задачи и валидация изменений
    get_task_response = api.get_task(task_id)
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    assert get_task_data['content'] == new_payload['content']
    assert get_task_data['user_id'] == new_payload['user_id']


def test_can_delete_task(new_task_payload):
    # создание задачи
    payload = new_task_payload
    create_task_response = api.create_task(payload=payload)
    assert create_task_response.status_code == 200
    task_id = create_task_response.json()['task']['task_id']

    # удаление задачи
    delete_task_response = api.delete_task(task_id=task_id)
    assert delete_task_response.status_code == 200

    # получение задачи и проверка того, что она не существует
    get_task_response = api.get_task(task_id=task_id)
    assert get_task_response.status_code == 404


def test_can_list_tasks(new_task_payload):
    # создание N задач
    n = 3
    payload = new_task_payload
    for _ in range(n):
        create_task_response = api.create_task(payload)
        assert create_task_response.status_code == 200

    # список задач и проверка на то, что там N элементов
    user_id = payload['user_id']
    list_tasks_response = api.list_tasks(user_id=user_id)
    assert list_tasks_response.status_code == 200
    data = list_tasks_response.json()

    tasks = data['tasks']
    assert len(tasks) == n
    print(data)
