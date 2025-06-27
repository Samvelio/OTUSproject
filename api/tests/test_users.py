import pytest
import allure
from api.client.reqres_client import ReqresClient
from config import UIConfig
from api.schemas.user_schema import UserResponse, UserListResponse

client = ReqresClient()

@allure.feature("Users API")
class TestUsers:
    @allure.title("Get user list")
    @pytest.mark.parametrize("page", [1, 2])
    def test_get_user_list(self, page):
        response = client.get_users(page)
        assert response.status_code == 200
        UserListResponse.parse_obj(response.json())

    @allure.title("Get single user")
    def test_get_single_user(self):
        response = client.get_user(2)
        assert response.status_code == 200
        UserResponse.parse_obj(response.json())

    @allure.title("User not found")
    def test_user_not_found(self):
        response = client.get_user(23)
        assert response.status_code == 404

    @allure.title("Create user")
    def test_create_user(self):
        user_data = {"name": "morpheus", "job": "leader"}
        response = client.create_user(user_data)
        assert response.status_code == 201
        assert response.json()["name"] == user_data["name"]

    @allure.title("Update user")
    @pytest.mark.parametrize("method", ["PUT", "PATCH"])
    def test_update_user(self, method):
        user_data = {"name": "morpheus", "job": "zion resident"}
        if method == "PUT":
            response = client.update_user(2, user_data)
        else:
            response = client.update_user(2, user_data)
        assert response.status_code == 200
        assert response.json()["job"] == user_data["job"]

    @allure.title("Delete user")
    def test_delete_user(self):
        response = client.delete_user(2)
        assert response.status_code == 204

