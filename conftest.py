import pytest
from api.courier_api import CourierApi
from helpers import generate_courier_payload

@pytest.fixture
def register_and_clean_courier():
    api = CourierApi()
    payload = generate_courier_payload()
    api.create_courier(payload)
    login_response = api.login_courier(payload)
    courier_id = login_response.json()["id"]
    yield payload
    api.delete_courier(courier_id)