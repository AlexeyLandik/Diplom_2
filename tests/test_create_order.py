import allure
import requests
from ..urls import Urls
from ..data import Data


class TestCreateOrder:
    @allure.title('Успешное создание заказа авторизованным пользователем')
    def test_create_order_by_auth_user(self, user):
        token = requests.post(Urls.CREATE_USER, data=user).json()['accessToken']
        order = requests.post(Urls.CREATE_ORDER, headers={'Authorization': token}, data=Data.INGREDIENTS)
        assert order.status_code == 200 and order.json()["order"]["status"] == "done"

    @allure.title('Попытка создания заказа не авторизованным пользователем')
    def test_create_order_by_not_auth_user(self, user):
        order = requests.post(Urls.CREATE_ORDER, data=Data.INGREDIENTS)
        assert order.status_code == 200 and order.json()["name"] == "Краторный бургер"

    @allure.title('Попытка создания заказов без ингредиентов')
    def test_create_order_without_ingredients(self, user):
        token = requests.post(Urls.CREATE_USER, data=user).json()['accessToken']
        order = requests.post(Urls.CREATE_ORDER, headers={'Authorization': token}, data=Data.EMPTY_INGREDIENTS)
        assert order.status_code == 400 and order.text == Data.RESPONSE_CREATE_ORDER_WITHOUT_INGREDIENTS

    @allure.title('Попытка создания заказа с невалидным хешем ингредиента')
    def test_create_order_with_not_valid_ingredient(self, user):
        token = requests.post(Urls.CREATE_USER, data=user).json()['accessToken']
        order = requests.post(Urls.CREATE_ORDER, headers={'Authorization': token}, data=Data.NOT_VALID_INGREDIENTS)
        assert order.status_code == 500
