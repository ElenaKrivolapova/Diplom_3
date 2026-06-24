import allure

from pages.base_page import BasePage

from locators.reset_password_page_locators import (
    ResetPasswordPageLocators
)

from urls import RESET_PASSWORD_URL


class ResetPasswordPage(BasePage):

    @allure.step('Открыть страницу сброса пароля')
    def open(self):

        self.open_page(
            RESET_PASSWORD_URL
        )

    @allure.step('Ввести новый пароль')
    def set_password(self, password):

        self.set_text(
            ResetPasswordPageLocators.PASSWORD_INPUT,
            password
        )

    @allure.step('Ввести код из письма')
    def set_code(self, code):

        self.set_text(
            ResetPasswordPageLocators.CODE_INPUT,
            code
        )

    @allure.step('Нажать кнопку показать/скрыть пароль')
    def click_show_password(self):

        self.click_element(
            ResetPasswordPageLocators.PASSWORD_SHOW_BUTTON
        )

    @allure.step('Нажать кнопку Сохранить')
    def click_save(self):

        self.click_element(
            ResetPasswordPageLocators.SAVE_BUTTON
        )

    @allure.step('Проверить, что поле пароля стало активным')
    def is_password_field_active(self):

        return self.is_element_visible(
            ResetPasswordPageLocators.ACTIVE_PASSWORD_CONTAINER
        )

    @allure.step('Проверить открытие страницы сброса пароля')
    def is_reset_password_page_opened(self):

        return self.is_element_visible(
            ResetPasswordPageLocators.RESET_PASSWORD_HEADER
        )