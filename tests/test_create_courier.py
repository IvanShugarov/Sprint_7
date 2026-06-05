from api.courier_api import CourierApi
from data import generate_courier_payload

class TestCreateCourier:
    def test_create_courier(self):
        api = CourierApi()
        payload = generate_courier_payload()
        response = api.create_courier(payload)
        assert response.status_code == 201 and response.json() == {"ok": True}

    def test_create_duplicate_courier_error(self):
        api = CourierApi()
        payload = generate_courier_payload()
        api.create_courier(payload)
        response = api.create_courier(payload)
        assert response.status_code == 409 and "Этот логин уже используется" in response.json()["message"]

    def test_create_courier_without_login_error(self):
        api = CourierApi()
        payload = generate_courier_payload()
        del payload["login"]
        response = api.create_courier(payload)
        assert response.status_code == 400 and "Недостаточно данных для создания учетной записи" in response.json()["message"]

    def test_create_courier_without_password_error(self):
        api = CourierApi()
        payload = generate_courier_payload()
        del payload["password"]
        response = api.create_courier(payload)
        assert response.status_code == 400 and "Недостаточно данных для создания учетной записи" in response.json()["message"] 
