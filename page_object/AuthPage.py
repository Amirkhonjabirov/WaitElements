from selenium.webdriver.common.by import By
from page_object.MainConst import MainConst
import allure

FIRSTNAME = (By.CSS_SELECTOR, "input[type='text'][name='firstname']")
LASTNAME = (By.CSS_SELECTOR, "input[type='text'][name='lastname']")
PASSWORD = (By.CSS_SELECTOR, "input[type='password'][name='password']")
CONF_PASS = (By.CSS_SELECTOR, "input[type='password'][name='confirm']")
MAIL = (By.CSS_SELECTOR, "input[type='email'][name='email']")
TEL = (By.CSS_SELECTOR, "input[type='tel'][name='telephone']")
LIST = (By.CSS_SELECTOR, "div[class='list-group']")
SUBMIT = (By.CSS_SELECTOR, "input[type='Submit']")
CHECK = (By.CSS_SELECTOR, "input[type='checkbox'][name='agree']")
RESULT = (By.CSS_SELECTOR, "#content > h1")


class AuthPage(MainConst):
    def auth_user(self, fname: str, lname: str, mail, tel: int, passw):
        with allure.step("Authorithing user"):
            try:
                with allure.step("Input Firstname"):
                    self._input(self.pres_element(FIRSTNAME), fname)
                with allure.step("Input Lastname"):
                    self._input(self.pres_element(LASTNAME), lname)
                with allure.step("Input Mail"):
                    self._input(self.pres_element(MAIL), mail)
                with allure.step("Input Tel"):
                    self._input(self.pres_element(TEL), tel)
                with allure.step("Input password"):
                    self._input(self.pres_element(PASSWORD), passw)
                with allure.step("Confirm Password"):
                    self._input(self.pres_element(CONF_PASS), passw)
                with allure.step("tap on checkbox"):
                    self.click(self.visible_element(CHECK))
                with allure.step("Submit"):
                    self.click(self.elem_clickble(SUBMIT))
                    return self
            except NoSuchElementException as y:
                allure.attach(body=self.driver.get_screenshot_as_png())
            raise AssertionError(y.msg)
