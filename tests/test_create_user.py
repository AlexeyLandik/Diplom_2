import requests
import allure
from ..data import Data
from ..urls import Urls


class TestCreateUser:
    @allure.title('Успешная регистрация нового пользователя: статус-код 200, тело ответа соответствует документации')
    def test_create_user(self, user):
        response = requests.post(Urls.CREATE_USER, data=user)
        assert response.status_code == 200 and Data.RESPONSE_KEYS_FOR_SUCCESS_REGISTRATION_AND_LOGIN in response.text

    @allure.title('Попытка регистрации существующего пльзователя: статус-код 403, тело ответа соответствует документации')
    def test_create_existing_user(self, user):
        requests.post(Urls.CREATE_USER, data=user)
        response = requests.post(Urls.CREATE_USER, data=user)
        assert response.status_code == 403 and response.text == Data.RESPONSE_FOR_REGISTRATION_EXISTING_USER

    @allure.title('Попытка регистрации пльзователя без email: статус-код 403, тело ответа соответствует документации')
    def test_create_user_without_email(self, user):
        user['email'] = ''
        response = requests.post(Urls.CREATE_USER, data=user)
        assert response.status_code == 403 and response.text == Data.RESPONSE_FOR_USER_WITHOUT_EMAIL
