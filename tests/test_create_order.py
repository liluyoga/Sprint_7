import requests
import json
import pytest
from data import AdditionalVariables, OrderData
import allure


class TestCreateOrder:
    @allure.title("Проверки, что можно указывать различные варианты цвета самоката в заказе")
    @pytest.mark.parametrize("order_data", [
        OrderData.order_data_1,
        OrderData.order_data_2,
        OrderData.order_data_3,
        OrderData.order_data_4
    ])
    def test_create_order_various_colors_success(self, order_data):
        headers = {"Content-type": "application/json"}
        response = requests.post(f'{AdditionalVariables.URL}/api/v1/orders', headers=headers, data=json.dumps(order_data))
        assert response.status_code == 201 and 'track' in response.text
