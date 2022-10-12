from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class MainConst:
    def __init__(self, driver):
        self.driver = driver

    def visible_element(self, locator: tuple):
        try:
            return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Не дождался видимости элемента {locator}")

    def pres_element(self, locator: tuple):
        try:
            return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"элемент {locator} не найден")

    def elem_clickble(self, locator: tuple):
        try:
            return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            raise AssertionError(f"элемент {locator} не кликабелен")

    def title(self, locator):
        try:
            return WebDriverWait(self.driver, 5).until(EC.title_is(locator))
        except TimeoutException:
            raise AssertionError(f"текст {locator} не корректен")

    def text_presnc(self, locator: tuple, txt):
        try:
            return WebDriverWait(self.driver, 5).until(EC.text_to_be_present_in_element(locator, txt))
        except TimeoutException:
            raise AssertionError(f"текст {txt} отсутствует")

    def click(self, element):
        ActionChains(self.driver).move_to_element(element).pause(0.1).click().perform()

    def _input(self, element, value):
        self.click(element)
        element.clear()
        element.send_keys(value)

    def alert(self):
        try:
            WebDriverWait(self.driver, 2).until(EC.alert_is_present())
            return self.driver.switch_to.alert
        except NoAlertPresentException:
            raise AssertionError(f"Didn't wait for alert to be visible")
