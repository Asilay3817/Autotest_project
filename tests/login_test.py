from selenium import webdriver
from pages.login_page import LoginPage



def test_positive_flou_login():
    from selenium.webdriver.chrome.options import Options
    o = Options()
    o.add_experimental_option("detach", True)
    o.add_argument("--headless")
    o.add_argument("--window-size=1800,900")
    driver = webdriver.Chrome(options=o)

    print('\nStart test')

    lp = LoginPage(driver)
    lp.sign_in()


    driver.close()
    driver.quit()

def test_login_is_empty():
    from selenium.webdriver.chrome.options import Options
    o = Options()
    o.add_experimental_option("detach", True)
    o.add_argument("--headless")
    o.add_argument("--window-size=1800,900")
    driver = webdriver.Chrome(options=o)

    print('\nStart test')

    lp = LoginPage(driver)
    lp.sign_in_with_empty_login()


    driver.close()
    driver.quit()


def test_password_is_empty():
    from selenium.webdriver.chrome.options import Options
    o = Options()
    o.add_experimental_option("detach", True)
    o.add_argument("--headless")
    o.add_argument("--window-size=1800,900")
    driver = webdriver.Chrome(options=o)

    print('\nStart test')

    lp = LoginPage(driver)
    lp.sign_in_with_empty_password()


    driver.close()
    driver.quit()









