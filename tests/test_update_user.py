import requests
import allure
from ..data import Data
from ..urls import Urls


class TestUpdateUser:
    @allure.title('Успешное изменение данных залогиненного пользователя: статус-код 200, тело ответа соответствует '
                  'документации')
    def test_update_logined_user(self, user):
        token = requests.post(Urls.CREATE_USER, data=user).json()['accessToken']
        requests.post(Urls.LOGIN_USER, data=user)
        response = requests.patch(Urls.UPDATE_USER, headers={'Authorization': token}, data=Data.CHANGED_USER_DATA)
        requests.delete(Urls.DELETE_USER, headers={'Authorization': token}, data=Data.CHANGED_USER_DATA)
        assert response.status_code == 200 and response.text == Data.RESPONSE_AFTER_SUCCESS_CHANGED_LOGINED_USER_DATA

    @allure.title('Попытка изменения данных не залогиненного пользователя: статус-код 401, тело ответа соответствует '
                  'документации')
    def test_update_registered_user(self, user):
        token = requests.post(Urls.CREATE_USER, data=user).json()['accessToken']
        response = requests.patch(Urls.UPDATE_USER, data=Data.CHANGED_USER_DATA)
        requests.delete(Urls.DELETE_USER, headers={'Authorization': token}, data=Data.CHANGED_USER_DATA)
        assert (response.status_code == 401 and
                response.text == Data.RESPONSE_AFTER_NOT_SUCCESS_CHANGED_NOT_LOGINED_USER_DATA)

    @allure.title('Попытка изменения данных залогиненного пользователя c другой почтой: статус-код 401, тело ответа '
                  'соответствует документации')
    def test_update_user_data_with_exist_email(self, user):
        token = requests.post(Urls.CREATE_USER, data=user).json()['accessToken']
        user['email'] = Data.EXIST_EMAIL
        response = requests.patch(Urls.UPDATE_USER, headers={'Authorization': token}, data=user)
        requests.delete(Urls.DELETE_USER, headers={'Authorization': token}, data=Data.CHANGED_USER_DATA)
        assert response.status_code == 403 and response.text == Data.RESPONSE_AFTER_NOT_SUCCESS_CHANGED_USER_DATA_EXIST_EMAIL
