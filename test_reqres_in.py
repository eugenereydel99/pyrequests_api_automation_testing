import allure
import pytest

from models.Enpoints import ReqresInEndpoint
from models.Register import RegisterRequest, RegisterResponseSuccess, RegisterResponseError
from models.Resource import Resource
from models.User import User


@pytest.mark.reqres_in
@allure.suite(
    suite_name="Test-suite №1"
)
@allure.severity(allure.severity_level.NORMAL)
class TestReqresInFirst:
    @allure.description(test_description=
                        "Тест проверяет вхождение id пользователя в название его изображения"
                        )
    def test_user_id_matches_the_name_of_the_avatar_file(self, api_client):
        response = api_client.get_request(ReqresInEndpoint.list_of_users).json()["data"]
        users = [User(**user) for user in response]
        for user in users:
            assert str(user.id) in user.avatar

    @allure.description(test_description=
                        "Тест проверяет вхождение определенного почтового домена в атрибуте 'email'"
                        )
    def test_user_email_contains_specific_domain(self, api_client):
        response = api_client.get_request(ReqresInEndpoint.list_of_users).json()["data"]
        users = [User(**user) for user in response]
        for user in users:
            assert user.email.endswith("@reqres.in")


@pytest.mark.reqres_in
@allure.description(
    test_description="Тест-кейс 2"
)
@allure.severity(allure.severity_level.NORMAL)
class TestReqresInSecond:
    @pytest.mark.positive
    def test_user_can_successfully_register(self, api_client):
        expected_id = 4
        expected_token = "QpwL5tke4Pnpja7X4"
        user = RegisterRequest(email="eve.holt@reqres.in", password="pistol")
        response = api_client.post_request(
            endpoint=ReqresInEndpoint.create_user,
            body=user.dict()
        )
        success_register = RegisterResponseSuccess(**response.json())
        assert response.status_code == 200
        assert success_register.id == expected_id
        assert success_register.token, expected_token

    @pytest.mark.negative
    def test_user_cant_successfully_register(self, api_client):
        user = RegisterRequest(email="sydney@fife", password="")
        response = api_client.post_request(
            endpoint=ReqresInEndpoint.create_user,
            body=user.dict()
        )
        error_register = RegisterResponseError(**response.json())
        assert response.status_code == 400
        assert error_register.error == "Missing password"


@pytest.mark.reqres_in
@allure.description(
    test_description="Тест-кейс 3"
)
@allure.severity(allure.severity_level.NORMAL)
class TestReqresInThird:
    def test_list_of_resource_is_sorted(self, api_client):
        response = api_client.get_request(
            ReqresInEndpoint.list_of_resources
        ).json()["data"]
        resources: list[int] = [
            Resource(**resource).year for resource in response
        ]
        sorted_resources = sorted(resources)
        assert resources == sorted_resources


@pytest.mark.reqres_in
@allure.description(
    test_description="Тест-кейс 4"
)
@allure.severity(allure.severity_level.CRITICAL)
class TestReqresInFourth:
    def test_can_delete_specific_user(self, api_client):
        response = api_client.delete_request(
            ReqresInEndpoint.delete_user
        )
        assert response.status_code == 204
