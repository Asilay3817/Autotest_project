from selenium import webdriver

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.finish_page import FinishPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.overview_page import OverviewPage


def test_by_product1():
    from selenium.webdriver.chrome.options import Options
    o = Options()
    o.add_experimental_option("detach", True)
    o.add_argument("--headless")
    o.add_argument("--window-size=1800,900")
    driver = webdriver.Chrome(options=o)

    print('\nStart test')

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









