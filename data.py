import random
import string


class AdditionalVariables:
    URL = 'https://qa-scooter.praktikum-services.ru'


class NewCourierData:

    @staticmethod
    def new_courier_data_without_login():
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        pass_first_name = {}

        password = generate_random_string(10)
        first_name = generate_random_string(10)

        pass_first_name["password"] = password
        pass_first_name["first_name"] = first_name

        return pass_first_name

    @staticmethod
    def new_courier_data_without_password():
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        login_first_name = {}

        login = generate_random_string(10)
        first_name = generate_random_string(10)

        login_first_name["login"] = login
        login_first_name["first_name"] = first_name

        return login_first_name


class OrderData:
    order_data_1 = {
        "firstName": "Йода",
        "lastname": "Джедай",
        "address": "планета Дагоба",
        "metroStation": 3,
        "phone": "+79991123344",
        "rentTime": 2,
        "deliveryDate": "2024-03-25",
        "comment": "Терпение необходимо во всем, что вы делаете",
        "color": [
            "BLACK"
        ]
    }

    order_data_2 = {
        "firstName": "Йода",
        "lastname": "Джедай",
        "address": "планета Дагоба",
        "metroStation": 3,
        "phone": "+79991123344",
        "rentTime": 2,
        "deliveryDate": "2024-03-25",
        "comment": "Терпение необходимо во всем, что вы делаете",
        "color": [
            "GREY"
        ]
    }

    order_data_3 = {
        "firstName": "Йода",
        "lastname": "Джедай",
        "address": "планета Дагоба",
        "metroStation": 3,
        "phone": "+79991123344",
        "rentTime": 2,
        "deliveryDate": "2024-03-25",
        "comment": "Терпение необходимо во всем, что вы делаете",
        "color": [
            "BLACK",
            "GREY"
        ]
    }

    order_data_4 = {
        "firstName": "Йода",
        "lastname": "Джедай",
        "address": "планета Дагоба",
        "metroStation": 3,
        "phone": "+79991123344",
        "rentTime": 2,
        "deliveryDate": "2024-03-25",
        "comment": "Терпение необходимо во всем, что вы делаете",
        "color": []
    }
