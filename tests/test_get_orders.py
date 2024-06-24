import allure
import requests
from ..urls import Urls
from ..data import Data


class TestGetOrders:
    @allure.title('Получение заказов авторизованнным пользователем')
    def test_get_orders_auth_user(self, user):
        token = requests.post(Urls.CREATE_USER, data=user).json()['accessToken']
        requests.post(Urls.CREATE_ORDER, headers={'Authorization': token}, data=Data.INGREDIENTS)
        requests.post(Urls.CREATE_ORDER, headers={'Authorization': token}, data=Data.INGREDIENTS)
        orders = requests.get(Urls.GET_ORDERS_BY_USER, headers={'Authorization': token})
        assert orders.status_code == 200 and len(orders.json()['orders']) == 2

    @allure.title('Попытка получения заказов не авторизованнным пользователем')
    def test_get_orders_not_auth_user(self, user):
        orders = requests.get(Urls.GET_ORDERS_BY_USER)
        assert orders.status_code == 401 and orders.text == Data.RESPONSE_GET_ORDERS_BY_NOT_AUTH_USER
