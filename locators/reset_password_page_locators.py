from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:

    # поле ввода нового пароля
    PASSWORD_INPUT = (
        By.XPATH,
        "//input[@name='Введите новый пароль']"
    )

    # контейнер активного поля пароля
    # после клика по глазику у контейнера появляется класс input_status_active
    ACTIVE_PASSWORD_CONTAINER = (
        By.XPATH,
        "//div[contains(@class,'input_status_active')]"
    )

    # кнопка показать / скрыть пароль
    PASSWORD_SHOW_BUTTON = (
        By.XPATH,
        "//div[contains(@class,'input__icon-action')]"
    )

    # поле ввода кода из письма
    CODE_INPUT = (
        By.XPATH,
        "//input[@name='Введите код из письма']"
    )

    # кнопка Сохранить
    SAVE_BUTTON = (
        By.XPATH,
        "//button[text()='Сохранить']"
    )

    # заголовок страницы
    RESET_PASSWORD_HEADER = (
        By.XPATH,
        "//h2[text()='Восстановление пароля']"
    )