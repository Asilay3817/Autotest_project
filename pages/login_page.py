from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

from utilities.logger import Logger


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
    error_message = "//div[@class='error-message-container error']"

    #Getters

    def get_username_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.username_field)))

    def get_password_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password_field)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_error_message(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.error_message)))



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
        with allure.step("Sign in"):
            Logger.add_start_step(method='sign_in')
            self.driver.get(self.url)
            self.send_login()
            self.assert_field_value(self.get_username_field(), self.login_name)
            self.send_password()
            self.assert_field_value(self.get_password_field(), self.login_password)
            self.click_login_button()
            self.get_current_url()
            self.assert_url('https://www.saucedemo.com/inventory.html')
            Logger.add_end_step(url=self.driver.current_url, method='sign_in')

    def sign_in_with_empty_login(self):
        with allure.step("Sign in with empty login"):
            Logger.add_start_step(method='sign_in_with_empty_login')
            self.driver.get(self.url)
            self.send_password()
            self.assert_field_value(self.get_password_field(), self.login_password)
            self.click_login_button()
            self.assert_error_message(self.get_error_message())
            Logger.add_end_step(url=self.driver.current_url, method='sign_in_with_empty_login')


    def sign_in_with_empty_password(self):
        with allure.step("Sign in with empty password"):
            Logger.add_start_step(method='sign_in_with_empty_password')
            self.driver.get(self.url)
            self.send_login()
            self.assert_field_value(self.get_username_field(), self.login_name)
            self.click_login_button()
            self.assert_error_message(self.get_error_message())
            Logger.add_end_step(url=self.driver.current_url, method='sign_in_with_empty_password')
