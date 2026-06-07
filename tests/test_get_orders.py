from api.order_api import OrdersApi
import allure

class TestGetOrder:
    @allure.title("Проверка успешного получения списка заказов")
    def test_get_order_list_success(self):
        api = OrdersApi()
        response = api.get_order_list()
        assert response.status_code == 200 and type(response.json()["orders"]) is list