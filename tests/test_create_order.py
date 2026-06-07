import pytest
from api.order_api import OrdersApi
import allure

class TestOrder:
    @allure.title("Проверка успешного заказа самоката")
    @pytest.mark.parametrize("color",[["GREY"],["BLACK"],["GREY","BLACK"],[]])
    def test_order(self,color):
        payload = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": color
}
        api = OrdersApi()
        response = api.create_order(payload)
        assert response.status_code == 201 and "track" in response.json()