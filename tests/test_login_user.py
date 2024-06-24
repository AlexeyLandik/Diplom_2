import requests
import allure
from ..data import Data
from ..urls import Urls
import pytest


class TestLoginUser:
    @allure.title('Успешная авторизация пользователя: статус-код 200, тело ответа соответствует документации')
    def test_login_user(self, user):
        requests.post(Urls.CREATE_USER, data=user)
        response = requests.post(Urls.LOGIN_USER, data=user)
        assert response.status_code == 200 and Data.RESPONSE_KEYS_FOR_SUCCESS_REGISTRATION_AND_LOGIN in response.text

    @allure.title('Попытка авторизации пользователя без email или password: статус-код 401, тело ответа соответствует '
                  'документации')
    @pytest.mark.parametrize(
        'empty_data',
        [
            'email',
            'password'
        ]
    )
    def test_login_user_without_email(self, user, empty_data):
        requests.post(Urls.CREATE_USER, data=user)
        user[empty_data] = ''
        response = requests.post(Urls.LOGIN_USER, data=user)
        assert response.status_code == 401 and response.text == Data.RESPONSE_FOR_LOGIN_USER_WITH_INCORRECT_EMAIL
