import allure

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.order_feed_page import OrderFeedPage
from pages.order_history_page import OrderHistoryPage


from urls import LOGIN_URL, PROFILE_URL


class TestOrderFeed:

    @allure.title('Открытие деталей заказа по клику')
    def test_open_order_details(self, driver):

        order_feed = OrderFeedPage(driver)

        order_feed.open()
        order_feed.open_first_order()

        assert order_feed.is_order_modal_opened()

    @allure.title('Заказ из истории отображается в ленте')
    def test_order_from_history_visible_in_feed(
        self,
        driver,
        authorized_user
    ):

        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)
        history_page = OrderHistoryPage(driver)
        order_feed = OrderFeedPage(driver)

        main_page.open()
        main_page.click_personal_account()
        main_page.wait_url_contains(LOGIN_URL)

        login_page.login(
            authorized_user['email'],
            authorized_user['password']
        )

        assert main_page.is_main_page_opened()

        main_page.add_first_bun_to_constructor()

        assert (main_page.get_first_bun_counter() == 2)

        main_page.wait_make_order_button()

        main_page.click_make_order()

        order_number = main_page.get_order_number()

        assert order_number.isdigit()
        assert order_number != '9999'

        main_page.close_order_modal()

        main_page.click_personal_account()
        main_page.wait_url_contains(PROFILE_URL)

        profile_page.click_order_history()

        assert history_page.is_order_history_opened()
        assert history_page.is_order_present(order_number)

        order_feed.open()

        assert order_feed.wait_order_in_feed(order_number)

    @allure.title('Счётчик Выполнено за всё время увеличивается')
    def test_total_done_counter_increases(
        self,
        driver,
        authorized_user
    ):

        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_feed = OrderFeedPage(driver)

        order_feed.open()

        before = order_feed.get_total_done_counter()

        main_page.open()
        main_page.click_personal_account()
        main_page.wait_url_contains(LOGIN_URL)

        login_page.login(
            authorized_user['email'],
            authorized_user['password']
        )

        main_page.add_first_bun_to_constructor()

        assert (main_page.get_first_bun_counter() == 2)

        main_page.wait_make_order_button()

        main_page.click_make_order()

        order_number = main_page.get_order_number()

        assert order_number.isdigit()
        assert order_number != '9999'

        order_feed.open()

        assert order_feed.wait_total_done_counter_more_than(before)

    @allure.title('Счётчик Выполнено за сегодня увеличивается')
    def test_today_done_counter_increases(
        self,
        driver,
        authorized_user
    ):

        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_feed = OrderFeedPage(driver)

        order_feed.open()

        before = order_feed.get_today_done_counter()

        main_page.open()
        main_page.click_personal_account()
        main_page.wait_url_contains(LOGIN_URL)

        login_page.login(
            authorized_user['email'],
            authorized_user['password']
        )

        main_page.add_first_bun_to_constructor()

        main_page.wait_make_order_button()

        main_page.click_make_order()

        order_number = main_page.get_order_number()

        assert order_number.isdigit()
        assert order_number != '9999'

        order_feed.open()

        assert order_feed.wait_today_done_counter_more_than(before)

    @allure.title('Новый заказ появляется в блоке В работе')
    def test_order_appears_in_progress(
        self,
        driver,
        authorized_user
    ):

        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_feed = OrderFeedPage(driver)

        main_page.open()
        main_page.click_personal_account()

        login_page.login(
            authorized_user['email'],
            authorized_user['password']
        )

        main_page.add_first_bun_to_constructor()

        main_page.wait_make_order_button()

        main_page.click_make_order()

        order_number = main_page.get_order_number()

        assert order_number.isdigit()
        assert order_number != '9999'

        order_feed.open()

        assert order_feed.wait_order_in_progress(order_number)