from api.courier_api import CourierApi
from helpers import register_new_courier_and_return_login_password as reg_new
import allure
from text_errors import MISSING_DATA_LOGIN, USER_NOT_FOUND
import pytest


class TestLoginCourier:
    @allure.title("Проверка входа в систему зарегистрированного курьера")
    def test_login_courier(self,register_and_clean_courier):
        api = CourierApi()
        response = api.login_courier(register_and_clean_courier)
        assert response.status_code == 200 and "id" in response.json()

    @allure.title("Проверка ошибк при входе в систему курьера без логина")
    def test_login_courier_without_login_error(self):
        api = CourierApi()
        courier = reg_new()
        payload = {"password":courier[1]}
        response = api.login_courier(payload)
        assert response.status_code == 400 and MISSING_DATA_LOGIN in response.json()["message"]
    
    @allure.title("Проверка ошибки при входе в систему курьера без пароля")
    def test_login_courier_without_password_error(self):
        api = CourierApi()
        courier = reg_new()
        payload = {"login":courier[0],"password":" "}
        response = api.login_courier(payload)
        assert response.status_code == 404 and USER_NOT_FOUND in response.json()["message"]

    @allure.title("Проверка ошибки входа в систему при неверном логине или пароле ")
    @pytest.mark.parametrize("invalid_payload",[{"login": "non_existent_user_123", "password": "correct_password"},{"login": "correct_login", "password": "wrong_password_aaaa"}])
    def test_login_courier_invalid_credentials_error(self,invalid_payload):
        api = CourierApi()
        response = api.login_courier(invalid_payload)
        assert response.status_code == 404 and USER_NOT_FOUND in response.json()["message"]

    @allure.title("Проверка ошибки при входе в систему несуществующего курьера")
    def test_login_with_non_existent_courier(self):
        api = CourierApi()
        payload = {"login":"aaaaaa","password":"bbbbbb"}
        response = api.login_courier(payload)
        assert response.status_code == 404 and USER_NOT_FOUND in response.json()["message"]