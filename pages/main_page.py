import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

from urls import BASE_URL


class MainPage(BasePage):

    @allure.step('Открыть главную страницу')
    def open(self):

        self.open_page(BASE_URL)

    @allure.step('Перейти в личный кабинет')
    def click_personal_account(self):

        self.click_element(
            MainPageLocators.PERSONAL_ACCOUNT_BUTTON
        )

    @allure.step('Нажать кнопку Войти в аккаунт')
    def click_login_account(self):

        self.click_element(
            MainPageLocators.LOGIN_ACCOUNT_BUTTON
        )

    @allure.step('Перейти в Конструктор')
    def click_constructor(self):

        self.click_element(
            MainPageLocators.CONSTRUCTOR_BUTTON
        )

    @allure.step('Перейти в Ленту заказов')
    def click_order_feed(self):

        self.click_element(
            MainPageLocators.ORDER_FEED_BUTTON
        )

    @allure.step('Проверить открытие главной страницы')
    def is_main_page_opened(self):

        return self.is_element_visible(
            MainPageLocators.MAIN_HEADER
        )
    
    @allure.step('Открыть детали ингредиента')
    def open_ingredient_details(
        self,
        ingredient_locator
    ):
        self.click_element(
            ingredient_locator
        )

    @allure.step('Закрыть окно деталей ингредиента')
    def close_ingredient_modal(self):

        self.click_element(
            MainPageLocators.MODAL_CLOSE_BUTTON
        )

    @allure.step('Проверить открытие окна деталей')
    def is_ingredient_modal_opened(self):

        return self.is_element_visible(
            MainPageLocators.INGREDIENT_MODAL
        )

    @allure.step('Получить значение каунтера')
    def get_counter_value(
        self,
        counter_locator
    ):

        return int(
            self.get_text(
                counter_locator
            )
        )

    @allure.step('Перетащить ингредиент в заказ')
    def add_ingredient_to_constructor(self, ingredient_locator):

        self.drag_and_drop(
            ingredient_locator,
            MainPageLocators.BURGER_CONSTRUCTOR_LIST
        )

    @allure.step('Прокрутить до секции')
    def scroll_to_section(
        self,
        section_locator
    ):

        self.scroll_to_element(
            section_locator
        )

    @allure.step('Нажать кнопку Оформить заказ')
    def click_make_order(self):
        self.click_element(
            MainPageLocators.MAKE_ORDER_BUTTON
        )

    @allure.step('Проверить закрытие окна деталей')
    def is_ingredient_modal_closed(self):

        return self.wait_invisibility(
            MainPageLocators.INGREDIENT_MODAL
        )
    
    @allure.step('Получить номер заказа')
    def get_order_number(self):

        self.wait_text_not_empty(
            MainPageLocators.ORDER_NUMBER
        )

        self.wait_text_not_equal(
            MainPageLocators.ORDER_NUMBER,
            '9999'
        )

        return self.get_text(
            MainPageLocators.ORDER_NUMBER
        )

    @allure.step('Открыть детали первой булки')
    def open_first_bun_details(self):

        self.open_ingredient_details(
            MainPageLocators.FIRST_BUN
        )

    @allure.step('Добавить первую булку в заказ')
    def add_first_bun_to_constructor(self):

        self.add_ingredient_to_constructor(
            MainPageLocators.FIRST_BUN
        )

    @allure.step('Добавить первый соус в заказ')
    def add_first_sauce_to_constructor(self):

        self.add_ingredient_to_constructor(
            MainPageLocators.FIRST_SAUCE
        )

    @allure.step('Добавить первую начинку в заказ')
    def add_first_filling_to_constructor(self):

        self.add_ingredient_to_constructor(
            MainPageLocators.FIRST_FILLING
        )

    @allure.step('Получить значение каунтера первой булки')
    def get_first_bun_counter(self):

        return self.get_counter_value(
            MainPageLocators.FIRST_BUN_COUNTER
        )

    @allure.step('Получить значение каунтера первого соуса')
    def get_first_sauce_counter(self):

        return self.get_counter_value(
            MainPageLocators.FIRST_SAUCE_COUNTER
        )

    @allure.step('Получить значение каунтера первой начинки')
    def get_first_filling_counter(self):

        return self.get_counter_value(
            MainPageLocators.FIRST_FILLING_COUNTER
        )

    @allure.step('Прокрутить до первого соуса')
    def scroll_to_first_sauce(self):

        self.scroll_to_section(
            MainPageLocators.FIRST_SAUCE
        )

    @allure.step('Прокрутить до первой начинки')
    def scroll_to_first_filling(self):

        self.scroll_to_section(
            MainPageLocators.FIRST_FILLING
        )

    @allure.step('Дождаться кнопки Оформить заказ')
    def wait_make_order_button(self):

        return self.wait_visibility(
            MainPageLocators.MAKE_ORDER_BUTTON
        )

    @allure.step('Проверить отображение номера заказа')
    def is_order_number_visible(self):

        return self.is_element_visible(
            MainPageLocators.ORDER_NUMBER
        )

    @allure.step('Закрыть модальное окно заказа')
    def close_order_modal(self):

        self.click_element(
            MainPageLocators.MODAL_CLOSE_BUTTON
        )