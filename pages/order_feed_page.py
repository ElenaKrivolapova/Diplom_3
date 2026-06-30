import allure

from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators

from urls import FEED_URL


class OrderFeedPage(BasePage):

    @allure.step('Открыть страницу Лента заказов')
    def open(self):

        self.open_page(FEED_URL)

    @allure.step('Проверить открытие страницы')
    def is_order_feed_opened(self):

        return self.is_element_visible(
            OrderFeedPageLocators.ORDER_FEED_HEADER
        )

    @allure.step('Открыть первый заказ')
    def open_first_order(self):

        self.click_element(
            OrderFeedPageLocators.FIRST_ORDER_CARD
        )

    @allure.step('Проверить открытие модального окна')
    def is_order_modal_opened(self):

        return self.is_element_visible(
            OrderFeedPageLocators.ORDER_DETAILS_MODAL
        )

    @allure.step('Закрыть модальное окно')
    def close_order_modal(self):

        self.click_element(
            OrderFeedPageLocators.MODAL_CLOSE_BUTTON
        )

    @allure.step('Получить номер первого заказа')
    def get_first_order_number(self):

        return (
            self.get_text(
                OrderFeedPageLocators.FIRST_ORDER_NUMBER
            )
            .replace('#', '')
        )

    @allure.step('Получить значение счётчика Выполнено за всё время')
    def get_total_done_counter(self):

        return int(
            self.wait_visibility(
                OrderFeedPageLocators.TOTAL_DONE_COUNTER
            ).text
        )

    @allure.step('Получить значение счётчика Выполнено за сегодня')
    def get_today_done_counter(self):

        return int(
            self.wait_visibility(
                OrderFeedPageLocators.TODAY_DONE_COUNTER
            ).text
        )

    @allure.step('Проверить наличие номера заказа в ленте')
    def is_order_in_feed(self, order_number):

        return order_number in self.get_page_source()

    @allure.step('Дождаться появления заказа в ленте')
    def wait_order_in_feed(self, order_number):

        return self.wait_text_in_page_source(
            order_number
        )
    @allure.step('Проверить наличие номера заказа в блоке В работе')
    def is_order_in_progress(self, order_number):

        text = self.wait_visibility(
            OrderFeedPageLocators.IN_PROGRESS_ORDERS
        ).text

        return order_number in text
    
    @allure.step('Дождаться появления заказа в блоке В работе')
    def wait_order_in_progress(self, order_number):

        return self.wait_text_in_element(
            OrderFeedPageLocators.IN_PROGRESS_ORDERS,
            order_number
        ) 
    
    @allure.step('Дождаться увеличения счётчика Выполнено за всё время')
    def wait_total_done_counter_more_than(self, value):

        return self.wait_counter_more_than(
            OrderFeedPageLocators.TOTAL_DONE_COUNTER,
            value
        )


    @allure.step('Дождаться увеличения счётчика Выполнено за сегодня')
    def wait_today_done_counter_more_than(self, value):

        return self.wait_counter_more_than(
            OrderFeedPageLocators.TODAY_DONE_COUNTER,
            value
        )