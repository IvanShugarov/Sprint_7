from api.courier_api import CourierApi
from helpers import generate_courier_payload
import allure
from text_errors import LOGIN_ALREADY_EXISTS,MISSING_DATA_CREATE

class TestCreateCourier:
    @allure.title("Проверка успешного создания курьера")
    def test_create_courier(self):
        api = CourierApi()
        payload = generate_courier_payload()
        response = api.create_courier(payload)
        assert response.status_code == 201 and response.json() == {"ok": True}
        login_response = api.login_courier(payload)
        courier_id = login_response.json()["id"]
        api.delete_courier(courier_id)

    @allure.title("Проверка ошибки при создания дубликата курьера")
    def test_create_duplicate_courier_error(self):
        api = CourierApi()
        payload = generate_courier_payload()
        api.create_courier(payload)
        response = api.create_courier(payload)
        assert response.status_code == 409 and LOGIN_ALREADY_EXISTS in response.json()["message"]

    @allure.title("Проверка ошибки при создании курьера без логина")
    def test_create_courier_without_login_error(self):
        api = CourierApi()
        payload = generate_courier_payload()
        del payload["login"]
        response = api.create_courier(payload)
        assert response.status_code == 400 and MISSING_DATA_CREATE in response.json()["message"]

    @allure.title("Проверка ошибки при создании курьера без пароля")
    def test_create_courier_without_password_error(self):
        api = CourierApi()
        payload = generate_courier_payload()
        del payload["password"]
        response = api.create_courier(payload)
        assert response.status_code == 400 and MISSING_DATA_CREATE in response.json()["message"] 
