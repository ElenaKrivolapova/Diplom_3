from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):

        # сохранить экземпляр браузера
        self.driver = driver

    def open_page(self, url):

        # открыть страницу
        self.driver.get(url)

    def find_element(self, locator):

        # найти элемент
        return self.driver.find_element(*locator)

    def click_element(self, locator):

        # дождаться кликабельности и кликнуть
        element = WebDriverWait(
            self.driver,
            10
        ).until(
            EC.element_to_be_clickable(locator)
        )

        self.driver.execute_script(
            'arguments[0].click();',
            element
        )

    def set_text(self, locator, text):

        # заполнить поле
        element = self.wait_visibility(locator)
        element.send_keys(text)

    def get_text(self, locator):

        # получить текст
        return self.find_element(locator).text

    def wait_visibility(self, locator, timeout=10):

        # дождаться появления элемента
        return WebDriverWait(
            self.driver,
            timeout
        ).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_url_contains(self, url_part, timeout=10):

        # дождаться изменения URL
        return WebDriverWait(
            self.driver,
            timeout
        ).until(
            EC.url_contains(url_part)
        )

    def is_element_visible(self, locator):

        # проверить отображение элемента
        return self.wait_visibility(
            locator
        ).is_displayed()

    def scroll_to_element(self, locator):

        # проскроллить до элемента
        element = self.find_element(locator)

        self.driver.execute_script(
            'arguments[0].scrollIntoView();',
            element
        )

    def drag_and_drop(
        self,
        source_locator,
        target_locator
    ):

        # HTML5 drag-and-drop нестабильно работает через ActionChains в Firefox,
        # поэтому отправляем drag/drop-события через JavaScript
        source = self.wait_visibility(source_locator)
        target = self.wait_visibility(target_locator)

        self.driver.execute_script(
            """
            const source = arguments[0];
            const target = arguments[1];

            const dataTransfer = new DataTransfer();

            source.dispatchEvent(new DragEvent('dragstart', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            }));

            target.dispatchEvent(new DragEvent('dragenter', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            }));

            target.dispatchEvent(new DragEvent('dragover', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            }));

            target.dispatchEvent(new DragEvent('drop', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            }));

            source.dispatchEvent(new DragEvent('dragend', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            }));
            """,
            source,
            target
        )

    def get_current_url(self):

        # получить текущий URL
        return self.driver.current_url

    def get_page_source(self):

        # получить html страницы
        return self.driver.page_source

    def wait_invisibility(
        self,
        locator,
        timeout=10
    ):

        # дождаться исчезновения элемента
        return WebDriverWait(
            self.driver,
            timeout
        ).until(
            EC.invisibility_of_element_located(locator)
        )
    
    def wait_text_not_empty(self, locator, timeout=20):

        # дождаться, что у элемента появился текст
        return WebDriverWait(
            self.driver,
            timeout
        ).until(
            lambda driver: self.get_text(locator) != ''
        )
    
    def wait_text_not_equal(self, locator, value, timeout=20):

        # дождаться, что текст изменился
        return WebDriverWait(
            self.driver,
            timeout
        ).until(
            lambda driver:
            self.get_text(locator) != value
        )
    
    def wait_text_in_page_source(self, text, timeout=20):

        # дождаться появления текста в html страницы
        return WebDriverWait(
            self.driver,
            timeout
        ).until(
            lambda driver: text in self.get_page_source()
        )
    def wait_text_in_element(self, locator, text, timeout=20):

        return WebDriverWait(
            self.driver,
            timeout
        ).until(
            lambda driver:
            text in self.wait_visibility(locator).text
        )
    def wait_counter_more_than(
        self,
        locator,
        value,
        timeout=20
    ):

        return WebDriverWait(
            self.driver,
            timeout
        ).until(
            lambda driver:
            int(self.wait_visibility(locator).text) > value
        )