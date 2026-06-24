import allure

from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators
from locators.login_page_locators import LoginPageLocators


class ProfilePage(BasePage):

    @allure.step('Перейти в Историю заказов')
    def click_order_history(self):

        self.click_element(
            ProfilePageLocators.ORDER_HISTORY_BUTTON
        )

    @allure.step('Нажать кнопку Выход')
    def click_logout(self):

        self.click_element(
            ProfilePageLocators.LOGOUT_BUTTON
        )

    @allure.step('Проверить активность вкладки Профиль')
    def is_profile_active(self):

        return self.is_element_visible(
            ProfilePageLocators.PROFILE_ACTIVE
        )

    @allure.step('Проверить открытие профиля')
    def is_profile_opened(self):

        return self.is_profile_active()

    @allure.step('Проверить активность вкладки История заказов')
    def is_order_history_active(self):

        return self.is_element_visible(
            ProfilePageLocators.ORDER_HISTORY_ACTIVE
        )

    @allure.step('Проверить открытие Истории заказов')
    def is_order_history_opened(self):

        return self.is_order_history_active()

    @allure.step('Проверить открытие страницы логина')
    def is_login_page_opened(self):

        return self.is_element_visible(
            LoginPageLocators.LOGIN_BUTTON
        )