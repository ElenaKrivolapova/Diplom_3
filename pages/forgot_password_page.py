import allure

from pages.base_page import BasePage

from locators.forgot_password_page_locators import (
    ForgotPasswordPageLocators
)

from urls import FORGOT_PASSWORD_URL


class ForgotPasswordPage(BasePage):

    @allure.step('Открыть страницу восстановления пароля')
    def open(self):

        self.open_page(
            FORGOT_PASSWORD_URL
        )

    @allure.step('Ввести email')
    def set_email(self, email):

        self.set_text(
            ForgotPasswordPageLocators.EMAIL_INPUT,
            email
        )

    @allure.step('Нажать кнопку Восстановить')
    def click_recover(self):

        self.click_element(
            ForgotPasswordPageLocators.RECOVER_BUTTON
        )

    @allure.step('Отправить форму восстановления')
    def recover_password(self, email):

        self.set_email(email)

        self.click_recover()

    @allure.step(
        'Проверить открытие страницы восстановления пароля'
    )
    def is_forgot_password_page_opened(self):

        return self.is_element_visible(
            ForgotPasswordPageLocators.FORGOT_PASSWORD_HEADER
        )