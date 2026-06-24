import allure

from pages.base_page import BasePage
from locators.order_history_page_locators import (
    OrderHistoryPageLocators
)


class OrderHistoryPage(BasePage):

    @allure.step('Перейти в Историю заказов')
    def open_order_history(self):

        self.click_element(
            OrderHistoryPageLocators.ORDER_HISTORY_BUTTON
        )

    @allure.step('Проверить открытие страницы История заказов')
    def is_order_history_opened(self):

        return self.wait_url_contains(
            '/account/order-history'
        )

    @allure.step('Получить номер первого заказа')
    def get_first_order_number(self):

        return (
            self.get_text(
                OrderHistoryPageLocators.FIRST_ORDER_NUMBER
            )
            .replace('#', '')
        )

    @allure.step('Проверить наличие заказа в истории')
    def is_order_present(self, order_number):

        return order_number in self.driver.page_source