from api.courier_api import CourierApi
from data import register_new_courier_and_return_login_password as reg_new


class TestLoginCourier:
    def test_login_courier(self):
        api = CourierApi()
        courier = reg_new()
        payload = {"login":courier[0],"password":courier[1]}
        response = api.login_courier(payload)
        assert response.status_code == 200 and "id" in response.json()

    def test_login_courier_without_login_error(self):
        api = CourierApi()
        courier = reg_new()
        payload = {"password":courier[1]}
        response = api.login_courier(payload)
        assert response.status_code == 400 and "Недостаточно данных для входа" in response.json()["message"]
    
    def test_login_courier_without_password_error(self):
        api = CourierApi()
        courier = reg_new()
        payload = {"login":courier[0],"password":" "}
        response = api.login_courier(payload)
        assert response.status_code == 404 and "Учетная запись не найдена" in response.json()["message"]

    def test_login_courier_with_wrong_password(self):
        api = CourierApi()
        courier = reg_new()
        payload = {"login":courier[0],"password":"aaaaaa"}
        response = api.login_courier(payload)
        assert response.status_code == 404 and "Учетная запись не найдена" in response.json()["message"]

    def test_login_courier_with_wrong_login(self):
        api = CourierApi()
        courier = reg_new()
        payload = {"login":"aaaaaa","password":courier[1]}
        response = api.login_courier(payload)
        assert response.status_code == 404 and "Учетная запись не найдена" in response.json()["message"]

    def test_login_with_existent_courier(self):
        api = CourierApi()
        payload = {"login":"aaaaaa","password":"bbbbbb"}
        response = api.login_courier(payload)
        assert response.status_code == 404 and "Учетная запись не найдена" in response.json()["message"]