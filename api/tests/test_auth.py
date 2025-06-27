import pytest
import allure
from api.client.reqres_client import ReqresClient

client = ReqresClient()

@allure.feature("Authentication API")
class TestAuth:
    @allure.title("Successful login")
    def test_successful_login(self):
        credentials = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
        response = client.login(credentials)
        assert response.status_code == 200
        assert "token" in response.json()

    @allure.title("Unsuccessful login")
    @pytest.mark.parametrize("credentials", [
        {"email": "peter@klaven"},
        {"password": "cityslicka"},
        {}
    ])
    def test_unsuccessful_login(self, credentials):
        response = client.login(credentials)
        assert response.status_code == 400
        assert "error" in response.json()

