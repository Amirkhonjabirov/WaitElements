from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_main(executer):
    w = WebDriverWait(executer, 3)
    executer.get(url=executer.base_url)
    w.until(EC.title_is("Your Store"))
    w.until(EC.presence_of_element_located((By.ID, "search")))
    w.until(EC.presence_of_element_located((By.ID, "cart")))
    w.until(EC.presence_of_element_located((By.ID, "category")))
    w.until(EC.presence_of_element_located((By.ID, "carousel0")))


def test_admin(executer):
    executer.get(url=f"{executer.base_url}admin")
    w = WebDriverWait(executer, 5)
    w.until(EC.title_is("Administration"))
    w.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "panel-title"), "Please enter your login details."))
    w.until(EC.presence_of_element_located((By.ID, "input-username")))
    w.until(EC.presence_of_element_located((By.ID, "input-password")))
    w.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "button[type='submit']"), "Login"))


def test_auth(executer):
    executer.get(url=f"{executer.base_url}/index.php?route=account/register")
    w = WebDriverWait(executer, 5)
    w.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                            "input[type='text'][name='firstname']")))
    w.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                            "input[type='text'][name='lastname']")))
    w.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                            "input[type='password'][name='password']")))

    w.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='list-group']")))
    w.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='Submit']")))


def test_catalog(executer):
    executer.get(url=f"{executer.base_url}laptop-notebook")
    w = WebDriverWait(executer, 5)
    w.until(EC.title_is("Laptops & Notebooks"))
    w.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "select[id='input-sort']")))
    w.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "select[id='input-limit']")))
    w.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                            "input[type='text'][name='search']")))


def test_product(executer):
    executer.get(url=f"{executer.base_url}tablet/samsung-galaxy-tab-10-1")
    w = WebDriverWait(executer, 5)
    w.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id='button-cart']")))
    w.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-original-title='Add to Wish List']")))
    w.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-original-title='Compare this Product']")))
    w.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='text'][id='input-quantity']")))
    w.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='rating']")))
