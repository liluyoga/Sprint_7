import requests
import json
import pytest
from data import AdditionalVariables, NewCourierData
import allure


class TestCreateCourier:

    @allure.title("Проверка, что курьера можно создать")
    def test_create_courier_with_correct_data_ok_true(self, generate_new_courier_login_password):
        payload = json.dumps(generate_new_courier_login_password)
        headers = {"Content-type": "application/json"}
        response = requests.post(f'{AdditionalVariables.URL}/api/v1/courier', headers=headers, data=payload)
        assert response.status_code == 201 and response.json()["ok"] == True

    @allure.title("Проверка, что нельзя создать двух одинаковых курьеров")
    def test_create_courier_with_same_data_conflict(self, generate_new_courier_login_password):
        payload = json.dumps(generate_new_courier_login_password)
        headers = {"Content-type": "application/json"}
        requests.post(f'{AdditionalVariables.URL}/api/v1/courier', headers=headers, data=payload)
        response = requests.post(f'{AdditionalVariables.URL}/api/v1/courier', headers=headers, data=payload)
        assert response.status_code == 409 and AdditionalVariables.CREATE_COURIER_CONFLICT_MESSAGE in response.json()["message"]

    @allure.title("Проверка, что для создания курьера нужно передать обязательные поля login и password")
    @pytest.mark.parametrize("courier_data",
                             [
                                 NewCourierData.new_courier_data_without_login(),
                                 NewCourierData.new_courier_data_without_password()
                             ]
                             )
    def test_create_courier_without_login_password_bad_request(self, courier_data):
        payload = json.dumps(courier_data)
        headers = {"Content-type": "application/json"}
        response = requests.post(f'{AdditionalVariables.URL}/api/v1/courier', headers=headers, data=payload)
        assert response.status_code == 400 and response.json()[
            "message"] == AdditionalVariables.CREATE_COURIER_BAD_REQUEST_MESSAGE
