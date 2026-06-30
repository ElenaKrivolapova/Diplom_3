import allure
import requests

from urls import (
    REGISTER_URL,
    LOGIN_URL,
    USER_URL
)


@allure.step('Создать пользователя')
def create_user(user_data):

    return requests.post(
        REGISTER_URL,
        json=user_data
    )


@allure.step('Авторизовать пользователя')
def login_user(user_data):

    return requests.post(
        LOGIN_URL,
        json=user_data
    )


@allure.step('Обновить пользователя')
def update_user(token, data):

    return requests.patch(
        USER_URL,
        headers={
            'Authorization': token
        },
        json=data
    )


@allure.step('Удалить пользователя')
def delete_user(token):

    return requests.delete(
        USER_URL,
        headers={
            'Authorization': token
        }
    )