import allure

from pages.main_page import MainPage
from pages.login_page import LoginPage

from locators.main_page_locators import MainPageLocators

from urls import (
    BASE_URL,
    LOGIN_URL,
    FEED_URL
)


class TestMainFunctionality:

    @allure.title('Переход по клику на Конструктор')
    def test_go_to_constructor(self, driver):

        main_page = MainPage(driver)

        driver.get(FEED_URL)

        main_page.click_constructor()
        main_page.wait_url_contains(BASE_URL)

        assert main_page.is_main_page_opened()

    @allure.title('Переход по клику на Лента заказов')
    def test_go_to_order_feed(self, driver):

        main_page = MainPage(driver)

        main_page.open()
        main_page.click_order_feed()
        main_page.wait_url_contains(FEED_URL)

        assert FEED_URL in main_page.get_current_url()

    @allure.title('Открытие модального окна с деталями ингредиента')
    def test_open_ingredient_modal(self, driver):

        main_page = MainPage(driver)

        main_page.open()
        main_page.open_ingredient_details(
            MainPageLocators.FIRST_BUN
        )

        assert main_page.is_ingredient_modal_opened()

    @allure.title('Закрытие модального окна с деталями ингредиента')
    def test_close_ingredient_modal(self, driver):

        main_page = MainPage(driver)

        main_page.open()
        main_page.open_ingredient_details(
            MainPageLocators.FIRST_BUN
        )

        assert main_page.is_ingredient_modal_opened()

        main_page.close_ingredient_modal()

        assert main_page.is_ingredient_modal_closed()

    @allure.title('Каунтер булки увеличивается после добавления в заказ')
    def test_bun_counter_increases_after_drag_and_drop(self, driver):

        main_page = MainPage(driver)

        main_page.open()

        main_page.add_ingredient_to_constructor(
            MainPageLocators.FIRST_BUN
        )

        assert main_page.get_counter_value(
            MainPageLocators.FIRST_BUN_COUNTER
        ) == 2

    @allure.title('Каунтер соуса увеличивается после добавления в заказ')
    def test_sauce_counter_increases_after_drag_and_drop(self, driver):

        main_page = MainPage(driver)

        main_page.open()
        main_page.scroll_to_section(
            MainPageLocators.FIRST_SAUCE
        )

        main_page.add_ingredient_to_constructor(
            MainPageLocators.FIRST_SAUCE
        )

        assert main_page.get_counter_value(
            MainPageLocators.FIRST_SAUCE_COUNTER
        ) == 1

    @allure.title('Каунтер начинки увеличивается после добавления в заказ')
    def test_filling_counter_increases_after_drag_and_drop(self, driver):

        main_page = MainPage(driver)

        main_page.open()
        main_page.scroll_to_section(
            MainPageLocators.FIRST_FILLING
        )

        main_page.add_ingredient_to_constructor(
            MainPageLocators.FIRST_FILLING
        )

        assert main_page.get_counter_value(
            MainPageLocators.FIRST_FILLING_COUNTER
        ) == 1

    @allure.title('Авторизованный пользователь может оформить заказ')
    def test_authorized_user_can_make_order(self, driver, authorized_user):

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

        main_page.add_ingredient_to_constructor(
            MainPageLocators.FIRST_BUN
        )

        main_page.scroll_to_section(
            MainPageLocators.FIRST_SAUCE
        )
        main_page.add_ingredient_to_constructor(
            MainPageLocators.FIRST_SAUCE
        )

        main_page.scroll_to_section(
            MainPageLocators.FIRST_FILLING
        )
        main_page.add_ingredient_to_constructor(
            MainPageLocators.FIRST_FILLING
        )

        main_page.click_make_order()

        assert main_page.is_element_visible(
            MainPageLocators.ORDER_NUMBER
        )