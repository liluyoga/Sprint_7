import requests
import allure
from data import AdditionalVariables

class TestGetOrders:

    @allure.title("Проверка, что в тело ответа возвращается список всех заказов")
    def test_get_all_orders_success(self):
        response = requests.get(f'{AdditionalVariables.URL}/api/v1/orders')
        assert 'orders' in response.text
