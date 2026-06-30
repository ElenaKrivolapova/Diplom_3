import allure

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage

from urls import (
    LOGIN_URL,
    PROFILE_URL,
    ORDER_HISTORY_URL
)


def open_profile_page(driver, authorized_user):

    main_page = MainPage(driver)
    login_page = LoginPage(driver)

    main_page.open()
    main_page.click_personal_account()
    main_page.wait_url_contains(LOGIN_URL)

    login_page.login(
        authorized_user['email'],
        authorized_user['password']
    )

    assert main_page.is_main_page_opened()

    main_page.click_personal_account()
    main_page.wait_url_contains(PROFILE_URL)


class TestProfile:

    @allure.title('Переход в личный кабинет')
    def test_go_to_profile_page(self, driver, authorized_user):

        profile_page = ProfilePage(driver)

        open_profile_page(driver, authorized_user)

        assert profile_page.is_profile_opened()

    @allure.title('Переход в Историю заказов')
    def test_go_to_order_history(self, driver, authorized_user):

        profile_page = ProfilePage(driver)

        open_profile_page(driver, authorized_user)

        profile_page.click_order_history()
        profile_page.wait_url_contains(ORDER_HISTORY_URL)

        assert profile_page.is_order_history_opened()

    @allure.title('Выход из аккаунта')
    def test_logout(self, driver, authorized_user):

        profile_page = ProfilePage(driver)
        login_page = LoginPage(driver)

        open_profile_page(driver, authorized_user)

        profile_page.click_logout()
        profile_page.wait_url_contains(LOGIN_URL)

        assert login_page.is_login_page_opened()