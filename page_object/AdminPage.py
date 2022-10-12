from selenium.webdriver.common.by import By
from page_object.MainConst import MainConst

ADMIN_TITLE = "Administration"
PANEL_TITLE = (By.CLASS_NAME, "panel-title")
ADMIN_USER = (By.ID, "input-username")
ADMIN_PASS = (By.ID, "input-password")
SUBMIT_LOG = (By.CSS_SELECTOR, "button[type='submit']")

CATALOGS = (By.ID, 'menu-catalog')
PRODUCTS = (By.LINK_TEXT, "Products")
PROD_NAME = (By.ID, "input-name1")
META = (By.ID, "input-meta-title1")
MODEL = (By.ID, "input-model")
SUCCESS = (By.CSS_SELECTOR, "#content > div.container-fluid > div.alert.alert-success.alert-dismissible")

ADD = (By.CSS_SELECTOR, "#content > div.page-header > div > div > a")
DATA = (By.LINK_TEXT, "Data")
FILTER = (By.ID, "input-name")
BUTTON_FILTER = (By.ID, "button-filter")
PROS = (By.CSS_SELECTOR, '#form-product > div > table > tbody > tr > td:nth-child(3)')
CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox'][name='selected[]']")
DELETE = (By.CSS_SELECTOR, "button[data-original-title='Delete']")


class AdminPage(MainConst):
    def logon(self, username, password):
        self._input(self.pres_element(ADMIN_USER), username)
        self._input(self.pres_element(ADMIN_PASS), password)
        self.click(self.elem_clickble(SUBMIT_LOG))
        return self

    def open_products(self):
        self.click(self.visible_element(CATALOGS))
        self.click(self.pres_element(PRODUCTS))

    def add_product(self, product: str):
        self.click(self.pres_element(ADD))
        self._input(self.pres_element(PROD_NAME), product)
        self._input(self.pres_element(META), product)
        self.click(self.pres_element(DATA))
        self._input(self.pres_element(MODEL), product)
        self.click(self.pres_element((By.CSS_SELECTOR, "button[data-original-title='Save']")))

    def del_product(self, product: str):
        self._input(self.pres_element(FILTER), product)
        self.click(self.pres_element(BUTTON_FILTER))
        assert self.text_presnc(PROS, product)
        self.click(self.pres_element(CHECKBOX))
        self.click(self.pres_element(DELETE))
        self.alert().accept()
