from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(Base):


    url = "https://www.saucedemo.com/"
    login_name = "standard_user"
    login_password = "secret_sauce"



    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators

    username_field = "//input[@id='user-name']"
    password_field = "//input[@id='password']"
    login_button = "//input[@id='login-button']"

    #Getters

    def get_username_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.username_field)))

    def get_password_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password_field)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))



    #Actions

    def click_username_field(self):
        self.get_username_field().click()
        print('Click username field')

    def click_password_field(self):
        self.get_password_field().click()
        print('Click password field')

    def click_login_button(self):
        self.get_login_button().click()
        print('Click login button')

    def send_login(self):
        self.get_username_field().send_keys(self.login_name)
        print('Send login')

    def send_password(self):
        self.get_password_field().send_keys(self.login_password)
        print('Send password')

    #Methods

    def sign_in(self):
        self.driver.get(self.url)
        # self.driver.maximize_window()
        self.click_username_field()
        self.send_login()
        self.assert_field_value(self.get_username_field(), self.login_name)
        self.click_password_field()
        self.send_password()
        self.assert_field_value(self.get_password_field(), self.login_password)
        self.click_login_button()
        self.get_current_url()
        self.assert_url('https://www.saucedemo.com/inventory.html')