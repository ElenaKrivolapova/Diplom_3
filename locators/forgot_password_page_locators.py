from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:

    # поле Email
    EMAIL_INPUT = (
        By.XPATH,
        "//input[@name='name']"
    )

    # кнопка Восстановить
    RECOVER_BUTTON = (
        By.XPATH,
        "//button[text()='Восстановить']"
    )

    # заголовок страницы
    FORGOT_PASSWORD_HEADER = (
        By.XPATH,
        "//h2[text()='Восстановление пароля']"
    )