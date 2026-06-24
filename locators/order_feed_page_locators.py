from selenium.webdriver.common.by import By


class OrderFeedPageLocators:

    # заголовок страницы Лента заказов
    ORDER_FEED_HEADER = (
        By.XPATH,
        "//h1[text()='Лента заказов']"
    )

    # первый заказ в ленте заказов
    FIRST_ORDER_CARD = (
        By.XPATH,
        "(//li[contains(@class,'OrderHistory_listItem')])[1]//a"
    )

    # номер первого заказа в ленте
    FIRST_ORDER_NUMBER = (
        By.XPATH,
        "(//p[contains(text(), '#')])[1]"
    )

    # модальное окно с деталями заказа
    ORDER_DETAILS_MODAL = (
        By.XPATH,
        "//section[contains(@class,'Modal_modal_opened')]"
    )

    # крестик закрытия модального окна
    MODAL_CLOSE_BUTTON = (
        By.XPATH,
        "//button[contains(@class,'Modal_modal__close')]"
    )

    TOTAL_DONE_COUNTER = (
        By.XPATH,
        "//p[contains(text(),'Выполнено за все время:')]/parent::div/p[contains(@class,'text_type_digits-large')]"
    )

    TODAY_DONE_COUNTER = (
        By.XPATH,
        "//p[contains(text(),'Выполнено за сегодня:')]/parent::div/p[contains(@class,'text_type_digits-large')]"
    )

    # список заказов в блоке Готовы
    READY_ORDERS = (
        By.XPATH,
        "//ul[contains(@class,'OrderFeed_orderList') and not(contains(@class,'Ready'))]"
    )

    IN_PROGRESS_ORDERS = (
        By.XPATH,
        "//ul[contains(@class,'OrderFeed_orderListReady')]"
    )