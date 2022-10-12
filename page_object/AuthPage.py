from selenium.webdriver.common.by import By
from page_object.MainConst import MainConst

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
        self._input(self.pres_element(FIRSTNAME), fname)
        self._input(self.pres_element(LASTNAME), lname)
        self._input(self.pres_element(MAIL), mail)
        self._input(self.pres_element(TEL), tel)
        self._input(self.pres_element(PASSWORD), passw)
        self._input(self.pres_element(CONF_PASS), passw)
        self.click(self.visible_element(CHECK))
        self.click(self.elem_clickble(SUBMIT))
        return self
