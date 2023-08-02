import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from conftest import set_up

@pytest.mark.third
def test_login(set_up):
    from selenium.webdriver.chrome.options import Options
    o = Options()
    o.add_experimental_option("detach", True)
    o.add_argument("--headless")
    o.add_argument("--window-size=1800,900")
    driver = webdriver.Chrome(options=o)


    lp = LoginPage(driver)
    lp.sign_in()


    driver.close()
    driver.quit()


@pytest.mark.first
def test_login_user_field_is_empty(set_up):
    from selenium.webdriver.chrome.options import Options
    o = Options()
    o.add_experimental_option("detach", True)
    o.add_argument("--headless")
    o.add_argument("--window-size=1800,900")
    driver = webdriver.Chrome(options=o)


    lp = LoginPage(driver)
    lp.sign_in_with_empty_login()


    driver.close()
    driver.quit()


@pytest.mark.second
def test_login_password_field_is_empty(set_up):
    from selenium.webdriver.chrome.options import Options
    o = Options()
    o.add_experimental_option("detach", True)
    o.add_argument("--headless")
    o.add_argument("--window-size=1800,900")
    driver = webdriver.Chrome(options=o)


    lp = LoginPage(driver)
    lp.sign_in_with_empty_password()


    driver.close()
    driver.quit()









