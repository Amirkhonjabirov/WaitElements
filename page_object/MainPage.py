from selenium.webdriver.common.by import By

MAIN_TITLE = "Your Store"
M_SEARCH = (By.ID, "search")
CART = (By.ID, "cart")
CATS = (By.ID, "category")
ADS = (By.ID, "carousel0")
CURRENCY = (By.CSS_SELECTOR, "button[class='btn btn-link dropdown-toggle'][data-toggle='dropdown']")
USD = (By.CSS_SELECTOR, "button[name = 'USD']")
EUR = (By.CSS_SELECTOR, "button[name = 'EUR']")
GBP = (By.CSS_SELECTOR, "button[name = 'GBP']")
CART_SUM = (By.CSS_SELECTOR, "button[class='btn btn-inverse btn-block btn-lg dropdown-toggle'][data-toggle='dropdown']")

