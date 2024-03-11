import random
import string
import datetime


class AdditionalVariables:
    URL = 'https://qa-scooter.praktikum-services.ru'
    LOGIN_BAD_REQUEST_MESSAGE = 'Недостаточно данных для входа'
    LOGIN_NOT_FOUND_MESSAGE = 'Учетная запись не найдена'
    CREATE_COURIER_CONFLICT_MESSAGE = 'Этот логин уже используется'
    CREATE_COURIER_BAD_REQUEST_MESSAGE = 'Недостаточно данных для создания учетной записи'


class NewCourierData:

    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod
    def new_courier_data_without_login():

        pass_first_name = {}

        password = NewCourierData.generate_random_string(10)
        first_name = NewCourierData.generate_random_string(10)

        pass_first_name["password"] = password
        pass_first_name["first_name"] = first_name

        return pass_first_name

    @staticmethod
    def new_courier_data_without_password():

        login_first_name = {}

        login = NewCourierData.generate_random_string(10)
        first_name = NewCourierData.generate_random_string(10)

        login_first_name["login"] = login
        login_first_name["first_name"] = first_name

        return login_first_name


class OrderData:

    @staticmethod
    def generate_delivery_date():
        date = datetime.datetime.today() + datetime.timedelta(days=1)
        date = date.strftime("%Y-%m-%d")
        return date

    order_data_1 = {
        "firstName": "Йода",
        "lastname": "Джедай",
        "address": "планета Дагоба",
        "metroStation": 3,
        "phone": "+79991123344",
        "rentTime": 2,
        "deliveryDate": generate_delivery_date(),
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
        "deliveryDate": generate_delivery_date(),
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
        "deliveryDate": generate_delivery_date(),
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
        "deliveryDate": generate_delivery_date(),
        "comment": "Терпение необходимо во всем, что вы делаете",
        "color": []
    }
