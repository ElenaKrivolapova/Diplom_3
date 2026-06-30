from selenium.webdriver.common.by import By


class MainPageLocators:

    # кнопка "Конструктор" в шапке
    CONSTRUCTOR_BUTTON = (
        By.XPATH,
        "//p[text()='Конструктор']"
    )

    # кнопка "Лента Заказов" в шапке
    ORDER_FEED_BUTTON = (
        By.XPATH,
        "//p[text()='Лента Заказов']"
    )

    # кнопка "Личный Кабинет" в шапке
    PERSONAL_ACCOUNT_BUTTON = (
        By.XPATH,
        "//p[text()='Личный Кабинет']"
    )

    # кнопка "Войти в аккаунт" на главной странице
    LOGIN_ACCOUNT_BUTTON = (
        By.XPATH,
        "//button[text()='Войти в аккаунт']"
    )

    # заголовок главной страницы
    MAIN_HEADER = (
        By.XPATH,
        "//h1[text()='Соберите бургер']"
    )

    # первая булка
    FIRST_BUN = (
        By.XPATH,
        "//h2[text()='Булки']/following-sibling::ul[1]/a[1]"
    )

    # первый соус
    FIRST_SAUCE = (
        By.XPATH,
        "//h2[text()='Соусы']/following-sibling::ul[1]/a[1]"
    )

    # первая начинка
    FIRST_FILLING = (
        By.XPATH,
        "//h2[text()='Начинки']/following-sibling::ul[1]/a[1]"
    )

    # каунтер первой булки
    FIRST_BUN_COUNTER = (
        By.XPATH,
        "//h2[text()='Булки']/following-sibling::ul[1]/a[1]//p[contains(@class,'counter_counter__num')]"
    )

    # каунтер первого соуса
    FIRST_SAUCE_COUNTER = (
        By.XPATH,
        "//h2[text()='Соусы']/following-sibling::ul[1]/a[1]//p[contains(@class,'counter_counter__num')]"
    )

    # каунтер первой начинки
    FIRST_FILLING_COUNTER = (
        By.XPATH,
        "//h2[text()='Начинки']/following-sibling::ul[1]/a[1]//p[contains(@class,'counter_counter__num')]"
    )

    # модальное окно ингредиента
    INGREDIENT_MODAL = (
        By.XPATH,
        "//section[contains(@class,'Modal_modal_opened')]"
    )

    # заголовок модального окна
    INGREDIENT_MODAL_TITLE = (
        By.XPATH,
        "//h2[text()='Детали ингредиента']"
    )

    # крестик закрытия модального окна
    MODAL_CLOSE_BUTTON = (
        By.XPATH,
        "//button[contains(@class,'Modal_modal__close')]"
    )

    # зона конструктора, куда перетаскиваем ингредиенты
    BURGER_CONSTRUCTOR_LIST = (
        By.XPATH,
        "//ul[contains(@class,'BurgerConstructor_basket__list')]"
    )

    # кнопка Оформить заказ
    MAKE_ORDER_BUTTON = (
        By.XPATH,
        "//button[contains(., 'Оформить заказ')]"
    )

    # номер заказа в модальном окне
    ORDER_NUMBER = (
        By.XPATH,
        "//h2[contains(@class,'Modal_modal__title_shadow')]"
    )