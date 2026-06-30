from selenium.webdriver.common.by import By


class OrderHistoryPageLocators:

    # кнопка История заказов
    ORDER_HISTORY_BUTTON = (
        By.XPATH,
        "//a[@href='/account/order-history']"
    )

    # первый заказ в истории
    FIRST_ORDER_CARD = (
        By.XPATH,
        "(//li[contains(@class,'OrderHistory_listItem')])[1]"
    )

    # номер первого заказа
    FIRST_ORDER_NUMBER = (
        By.XPATH,
        "(//li[contains(@class,'OrderHistory_listItem')])[1]//p[contains(text(),'#')]"
    )