import requests
import random
import string
import pytest
from data import AdditionalVariables


@pytest.fixture(scope='function')
def generate_new_courier_login_password():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login_pass = {}

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    login_pass["login"] = login
    login_pass["password"] = password
    login_pass["first_name"] = first_name

    yield login_pass

    payload = {
        "login": login_pass.get("login"),
        "password": login_pass.get("password")
    }

    response = requests.post(f'{AdditionalVariables.URL}/api/v1/courier/login', data=payload)
    id_value = response.json()["id"]
    requests.delete(f'{AdditionalVariables.URL}/api/v1/courier/{id_value}')


@pytest.fixture(scope='function')
def register_new_courier_and_return_login_password():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login_pass = []

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(f'{AdditionalVariables.URL}/api/v1/courier', data=payload)

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    yield login_pass

    payload = {
        "login": login_pass[0],
        "password": login_pass[1]
    }

    response = requests.post(f'{AdditionalVariables.URL}/api/v1/courier/login', data=payload)
    id_value = response.json()["id"]
    requests.delete(f'{AdditionalVariables.URL}/api/v1/courier/{id_value}')
