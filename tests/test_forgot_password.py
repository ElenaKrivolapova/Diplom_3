import allure

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage

from urls import (
    LOGIN_URL,
    FORGOT_PASSWORD_URL,
    RESET_PASSWORD_URL
)
from data import TEST_EMAIL, TEST_PASSWORD


class TestForgotPassword:

    @allure.title('Переход на страницу восстановления пароля')
    def test_go_to_forgot_password_page(self, driver):

        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)

        main_page.open()

        # переход на страницу логина через кнопку Личный кабинет
        main_page.click_personal_account()
        main_page.wait_url_contains(LOGIN_URL)

        assert LOGIN_URL in main_page.get_current_url()

        login_page.click_recover_password()
        login_page.wait_url_contains(FORGOT_PASSWORD_URL)

        assert FORGOT_PASSWORD_URL in forgot_password_page.get_current_url()
        assert forgot_password_page.is_forgot_password_page_opened()

    @allure.title('Ввод email и клик по кнопке Восстановить')
    def test_set_email_and_click_recover(self, driver):

        forgot_password_page = ForgotPasswordPage(driver)
        reset_password_page = ResetPasswordPage(driver)

        forgot_password_page.open()
        forgot_password_page.recover_password(TEST_EMAIL)
        forgot_password_page.wait_url_contains(RESET_PASSWORD_URL)

        assert RESET_PASSWORD_URL in reset_password_page.get_current_url()
        assert reset_password_page.is_reset_password_page_opened()

    @allure.title('Клик по глазику делает поле пароля активным')
    def test_click_show_password_makes_password_field_active(self, driver):

        forgot_password_page = ForgotPasswordPage(driver)
        reset_password_page = ResetPasswordPage(driver)

        # сначала переходим на reset-password через корректный пользовательский флоу
        forgot_password_page.open()
        forgot_password_page.recover_password(TEST_EMAIL)
        forgot_password_page.wait_url_contains(RESET_PASSWORD_URL)

        reset_password_page.set_password(TEST_PASSWORD)
        reset_password_page.click_show_password()

        assert reset_password_page.is_password_field_active()