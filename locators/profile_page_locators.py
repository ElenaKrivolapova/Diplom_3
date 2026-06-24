from selenium.webdriver.common.by import By


class ProfilePageLocators:

    # кнопка Профиль
    PROFILE_BUTTON = (
        By.XPATH,
        "//a[text()='Профиль']"
    )

    # активная вкладка Профиль
    PROFILE_ACTIVE = (
        By.XPATH,
        "//a[contains(@class,'Account_link_active') and text()='Профиль']"
    )

    # кнопка История заказов
    ORDER_HISTORY_BUTTON = (
        By.XPATH,
        "//a[text()='История заказов']"
    )

    # активная вкладка История заказов
    ORDER_HISTORY_ACTIVE = (
        By.XPATH,
        "//a[contains(@class,'Account_link_active') and text()='История заказов']"
    )

    # кнопка Выход
    LOGOUT_BUTTON = (
        By.XPATH,
        "//button[text()='Выход']"
    )