from selenium.webdriver.common.by import By
from page_object.MainConst import MainConst
import allure

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
        with allure.step("Enter Username"):
            try:
                self._input(self.pres_element(ADMIN_USER), username)
            except NoSuchElementException as e:
                allure.attach(body=self.driver.get_screenshot_as_png())
                raise AssertionError(e.msg)

        with allure.step("Enter Password"):
            try:
                self._input(self.pres_element(ADMIN_PASS), password)
            except NoSuchElementException as r:
                allure.attach(body=self.driver.get_screenshot_as_png())
                raise AssertionError(r.msg)

        with allure.step("Submit"):
            self.click(self.elem_clickble(SUBMIT_LOG))
            return self

    def open_products(self):
        with allure.step("Open Catalog Page"):
            try:
                self.click(self.visible_element(CATALOGS))
            except NoSuchElementException as f:
                allure.attach(body=self.driver.get_screenshot_as_png())
                raise AssertionError(f.msg)

        with allure.step("Open Products Page"):
            try:
                self.click(self.pres_element(PRODUCTS))
            except NoSuchElementException as x:
                allure.attach(body=self.driver.get_screenshot_as_png())
                raise AssertionError(x.msg)

    def add_product(self, product: str):
        with allure.step("Click to Add Button"):
            try:
                self.click(self.pres_element(ADD))
            except NoSuchElementException as e:
                allure.attach(body=self.driver.get_screenshot_as_png())
            raise AssertionError(e.msg)

        with allure.step("Add Product Name and Meta"):
            try:
                self._input(self.pres_element(PROD_NAME), product)
                self._input(self.pres_element(META), product)
            except NoSuchElementException as x:
                allure.attach(body=self.driver.get_screenshot_as_png())
            raise AssertionError(x.msg)

        with allure.step("Add Data and Model"):
            try:
                self.click(self.pres_element(DATA))
                self._input(self.pres_element(MODEL), product)
            except NoSuchElementException as q:
                allure.attach(body=self.driver.get_screenshot_as_png())
            raise AssertionError(q.msg)

        with allure.step("Save"):
            try:
                self.click(self.pres_element((By.CSS_SELECTOR, "button[data-original-title='Save']")))
            except NoSuchElementException as y:
                allure.attach(body=self.driver.get_screenshot_as_png())
            raise AssertionError(y.msg)

    def del_product(self, product: str):
        with allure.step("Find Product"):
            self._input(self.pres_element(FILTER), product)
            self.click(self.pres_element(BUTTON_FILTER))
            assert self.text_presnc(PROS, product)
        with allure.step("Choose"):
            self.click(self.pres_element(CHECKBOX))
        with allure.step("Delete"):
            self.click(self.pres_element(DELETE))
            self.alert().accept()
