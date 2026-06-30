from selenium.webdriver.common.by import By


class LoginPageLocators:

    # поле Email
    EMAIL_INPUT = (
        By.XPATH,
        "//input[@name='name']"
    )

    # поле Пароль
    PASSWORD_INPUT = (
        By.XPATH,
        "//input[@name='Пароль']"
    )

    # кнопка Войти
    LOGIN_BUTTON = (
        By.XPATH,
        "//button[text()='Войти']"
    )

    # ссылка Восстановить пароль
    RECOVER_PASSWORD_BUTTON = (
        By.XPATH,
        "//a[text()='Восстановить пароль']"
    )

    # заголовок страницы
    LOGIN_HEADER = (
        By.XPATH,
        "//h2[text()='Вход']"
    )