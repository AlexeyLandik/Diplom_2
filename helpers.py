import random
import string
import allure


class User:

    @staticmethod
    @allure.step('Генерация случайной строки')
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod
    @allure.step('Получение случайных данных для создания пользователя')
    def user_datas_creation(length):
        email = User.generate_random_string(5) + '@yandex.ru'
        password = User.generate_random_string(length)
        name = User.generate_random_string(length)
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        return payload
