import requests
import json
from data import AdditionalVariables
import allure


class TestLoginCourier:

    @allure.title("Проверка, что курьер может авторизоваться")
    def test_login_courier_with_correct_data_success(self, register_new_courier_and_return_login_password):
        payload = {"login": register_new_courier_and_return_login_password[0],
                   "password": register_new_courier_and_return_login_password[1]}
        headers = {"Content-type": "application/json"}
        response = requests.post(f'{AdditionalVariables.URL}/api/v1/courier/login', headers=headers,
                                 data=json.dumps(payload))
        assert response.status_code == 200 and 'id' in response.text

    @allure.title("Проверка, что для авторизации нужно передать обязательное поле login")
    def test_login_courier_without_login_bad_request(self, register_new_courier_and_return_login_password):
        payload = {"login": "", "password": register_new_courier_and_return_login_password[1]}
        headers = {"Content-type": "application/json"}
        response = requests.post(f'{AdditionalVariables.URL}/api/v1/courier/login', headers=headers,
                                 data=json.dumps(payload))
        assert response.status_code == 400 and response.json()["message"] == AdditionalVariables.LOGIN_BAD_REQUEST_MESSAGE

    @allure.title("Проверка, что для авторизации нужно передать обязательное поле password")
    def test_login_courier_without_password_bad_request(self, register_new_courier_and_return_login_password):
        payload = {"login": register_new_courier_and_return_login_password[0], "password": ""}
        headers = {"Content-type": "application/json"}
        response = requests.post(f'{AdditionalVariables.URL}/api/v1/courier/login', headers=headers,
                                 data=json.dumps(payload))
        assert response.status_code == 400 and response.json()["message"] == AdditionalVariables.LOGIN_BAD_REQUEST_MESSAGE

    @allure.title("Проверка ошибки при попытке авторизоваться под несуществующим пользователем (неверный login)")
    def test_login_courier_with_incorrect_login_not_found(self, register_new_courier_and_return_login_password):
        payload = {"login": f'{register_new_courier_and_return_login_password[0]}1',
                   "password": register_new_courier_and_return_login_password[1]
                   }
        headers = {"Content-type": "application/json"}
        response = requests.post(f'{AdditionalVariables.URL}/api/v1/courier/login', headers=headers,
                                 data=json.dumps(payload))
        assert response.status_code == 404 and response.json()["message"] == AdditionalVariables.LOGIN_NOT_FOUND_MESSAGE

    @allure.title("Проверка ошибки при попытке авторизоваться с неверным паролем (password)")
    def test_login_courier_with_incorrect_password_not_found(self, register_new_courier_and_return_login_password):
        payload = {"login": register_new_courier_and_return_login_password[0],
                   "password": f'{register_new_courier_and_return_login_password[1]}1'
                   }
        headers = {"Content-type": "application/json"}
        response = requests.post(f'{AdditionalVariables.URL}/api/v1/courier/login', headers=headers,
                                 data=json.dumps(payload))
        assert response.status_code == 404 and response.json()["message"] == AdditionalVariables.LOGIN_NOT_FOUND_MESSAGE
