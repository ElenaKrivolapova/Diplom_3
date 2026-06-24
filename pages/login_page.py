import allure

from pages.base_page import BasePage

from locators.login_page_locators import LoginPageLocators

from urls import LOGIN_URL


class LoginPage(BasePage):

    @allure.step('Открыть страницу логина')
    def open(self):

        self.open_page(LOGIN_URL)

    @allure.step('Ввести email')
    def set_email(self, email):

        self.set_text(
            LoginPageLocators.EMAIL_INPUT,
            email
        )

    @allure.step('Ввести пароль')
    def set_password(self, password):

        self.set_text(
            LoginPageLocators.PASSWORD_INPUT,
            password
        )

    @allure.step('Нажать кнопку Войти')
    def click_login(self):

        self.click_element(
            LoginPageLocators.LOGIN_BUTTON
        )

    @allure.step('Выполнить авторизацию')
    def login(self, email, password):

        self.set_email(email)

        self.set_password(password)

        self.click_login()

    @allure.step('Перейти к восстановлению пароля')
    def click_recover_password(self):

        self.click_element(
            LoginPageLocators.RECOVER_PASSWORD_BUTTON
        )

    @allure.step('Проверить открытие страницы логина')
    def is_login_page_opened(self):

        return self.is_element_visible(
            LoginPageLocators.LOGIN_HEADER
        )