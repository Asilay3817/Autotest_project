import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.finish_page import FinishPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.overview_page import OverviewPage
from conftest import set_up

@allure.description("Test by product1")
def test_by_product1(set_up):
    from selenium.webdriver.chrome.options import Options
    service = Service(executable_path = '/Users/asilay/Desktop/study/QA/Autotest_project /chromedriver')
    o = Options()
    o.add_experimental_option("detach", True)
    o.add_argument("--headless")
    o.add_argument("--window-size=1800,900")
    driver = webdriver.Chrome(service=service, options=o)


    lp = LoginPage(driver)
    lp.sign_in()

    mp = MainPage(driver)
    mp.item_1_add_to_cart()

    cp = CartPage(driver)
    cp.to_order_item_1()

    chp = CheckoutPage(driver)
    chp.order_data_entry()

    op = OverviewPage(driver)
    op.finish_order()

    fp = FinishPage(driver)
    fp.back_home()


    driver.close()
    driver.quit()









