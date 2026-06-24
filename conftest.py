import random

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from user import create_user, delete_user


# запуск тестов в Chrome и Firefox
@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):

    browser = request.param

    # настройка Chrome
    if browser == 'chrome':

        options = ChromeOptions()

        driver = webdriver.Chrome(
            options=options
        )

    # настройка Firefox
    elif browser == 'firefox':

        options = FirefoxOptions()

        driver = webdriver.Firefox(
            options=options
        )

    # открыть окно браузера
    driver.maximize_window()

    yield driver

    # закрыть браузер после теста
    driver.quit()


# данные пользователя для тестов
@pytest.fixture
def user_data():

    random_number = random.randint(1000, 999999)

    return {
        'email': f'test{random_number}@mail.ru',
        'password': 'password123',
        'name': 'Elena'
    }


# создать пользователя через API перед тестом
@pytest.fixture
def authorized_user(user_data):

    response = create_user(user_data)

    token = response.json()['accessToken']

    # вернуть данные пользователя для UI-логина
    yield user_data

    # удалить пользователя после теста
    delete_user(token)