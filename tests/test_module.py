import pytest
from page_object.ProdPage import *
from page_object.CatalogPage import *
from page_object.AuthPage import *
from page_object.AdminPage import *
from page_object.MainPage import *


@allure.suite("Checking Elements in Main Page")
def test_main(executer):
    executer.get(url=executer.base_url)
    MainConst(executer).title(MAIN_TITLE)
    MainConst(executer).pres_element(M_SEARCH)
    MainConst(executer).pres_element(CART)
    MainConst(executer).pres_element(CATS)
    MainConst(executer).pres_element(ADS)


@allure.suite("Checking Elements in Admin Page")
def test_admin(executer):
    executer.get(url=f"{executer.base_url}admin")
    MainConst(executer).title(ADMIN_TITLE)
    MainConst(executer).text_presnc(PANEL_TITLE, "Please enter your login details.")
    MainConst(executer).pres_element(ADMIN_USER)
    MainConst(executer).pres_element(ADMIN_PASS)
    MainConst(executer).text_presnc(SUBMIT_LOG, "Login")


@allure.suite("Checking Elements in Auth Page")
def test_auth(executer):
    executer.get(url=f"{executer.base_url}/index.php?route=account/register")
    MainConst(executer).pres_element(FIRSTNAME)
    MainConst(executer).pres_element(LASTNAME)
    MainConst(executer).pres_element(PASSWORD)
    MainConst(executer).visible_element(LIST)
    MainConst(executer).elem_clickble(SUBMIT)


@allure.suite("Checking Elements in Catalog Page")
def test_catalog(executer):
    executer.get(url=f"{executer.base_url}laptop-notebook")
    MainConst(executer).title(CAT_TITLE)
    MainConst(executer).visible_element(SORT)
    MainConst(executer).visible_element(LIMIT)
    MainConst(executer).pres_element(SEARCH)


@allure.suite("Checking Elements in Product Page")
def test_product(executer):
    executer.get(url=f"{executer.base_url}tablet/samsung-galaxy-tab-10-1")
    MainConst(executer).elem_clickble(CART_BUTTON)
    MainConst(executer).elem_clickble(COMPARE)
    MainConst(executer).elem_clickble(ADD_TO_WISH)
    MainConst(executer).visible_element(QUANTITY)
    MainConst(executer).visible_element(RATING)


@allure.suite("Add product")
def test_add_prod(executer):
    executer.get(url=f"{executer.base_url}admin")
    AdminPage(executer) \
        .logon(username="user", password="bitnami") \
        .open_products()
    AdminPage(executer).add_product("iPHONE 16")
    assert AdminPage(executer).pres_element(SUCCESS)


@allure.suite("Delete Product")
def test_del_prod(executer):
    executer.get(url=f"{executer.base_url}admin")
    AdminPage(executer) \
        .logon(username="user", password="bitnami") \
        .open_products()
    AdminPage(executer).del_product("iPHONE 16")
    assert AdminPage(executer).pres_element(SUCCESS)


@allure.suite("Auth New User")
def test_auth_user(executer):
    executer.get(url=f"{executer.base_url}/index.php?route=account/register")
    AuthPage(executer).auth_user("amir123", "djab113", "amirhon89@mail.ru", "901000797", "1234561")
    assert AuthPage(executer).text_presnc(RESULT, "Your Account Has Been Created!")


@allure.suite("Change Currency")
@pytest.mark.parametrize('tex, cur', (('0.00€', EUR), ('$0.00', USD), ('£0.00', GBP)))
def test_change_currency(executer, tex, cur):
    executer.get(url=executer.base_url)
    MainConst(executer).click(MainConst(executer).elem_clickble(CURRENCY))
    MainConst(executer).click(MainConst(executer).visible_element(cur))
    assert MainConst(executer).text_presnc(CART_SUM, f"0 item(s) - {tex}")
