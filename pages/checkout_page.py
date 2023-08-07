from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from utilities.logger import Logger


class CheckoutPage(Base):

    name = "Alex"
    last_name = "P"
    postal_code = "236000"


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators

    first_name_field = "//input[@id='first-name']"
    last_name_field = "//input[@id='last-name']"
    postal_code_field = "//input[@id='postal-code']"
    continue_button = "//input[@id='continue']"

    #Getters

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name_field)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name_field)))

    def get_postal_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.postal_code_field)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))

    #Actions

    def click_first_name(self):
        self.get_first_name().click()
        print('Click first name field')

    def send_first_name(self):
        self.get_first_name().send_keys(self.name)
        print('Send first name')

    def click_last_name(self):
        self.get_last_name().click()
        print('Click last name field')

    def send_last_name(self):
        self.get_last_name().send_keys(self.last_name)
        print('Send last name')

    def click_postal_code(self):
        self.get_postal_code().click()
        print('Click postal code field')

    def send_postal_code(self):
        self.get_postal_code().send_keys(self.postal_code)
        print('Send postal code')

    def click_continue_button(self):
        self.get_continue_button().click()
        print('Click continue button')

    #Methods

    def order_data_entry(self):
        with allure.step("Order data entry"):
            Logger.add_start_step(method='order_data_entry')
            self.click_first_name()
            self.send_first_name()
            self.assert_field_value(self.get_first_name(), self.name)
            self.click_last_name()
            self.send_last_name()
            self.assert_field_value(self.get_last_name(), self.last_name)
            self.click_postal_code()
            self.send_postal_code()
            self.assert_field_value(self.get_postal_code(), self.postal_code)
            self.get_screenshot("checkout_page")
            self.click_continue_button()
            self.get_current_url()
            self.assert_url('https://www.saucedemo.com/checkout-step-two.html')
            Logger.add_end_step(url=self.driver.current_url, method='order_data_entry')