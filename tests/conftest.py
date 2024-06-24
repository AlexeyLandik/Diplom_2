import allure
import pytest
from ..helpers import User


@allure.step('Создание данных для уникального пользователя')
@pytest.fixture(scope='function')
def user():
    user = User()
    user_data = user.user_datas_creation(10)
    return user_data
