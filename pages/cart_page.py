from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from pages.main_page import MainPage
from utilities.logger import Logger


class CartPage(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators

    cart_item_1_value = "//div[@class='inventory_item_name']"
    cart_item_1_price = "//div[@class='inventory_item_price']"
    checkout_button = "//button[@id='checkout']"

    #Getters

    def get_cart_item_1_value(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_item_1_value)))

    def get_cart_item_1_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_item_1_price)))

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    #Actions

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print('Click checkout button')

    #Methods

    def to_order_item_1(self):
        with allure.step("To order item 1"):
            Logger.add_start_step(method='to_order_item_1')
            self.get_screenshot("cart_page")
            self.assert_item_text(MainPage(self.driver).get_item_1_value(), self.get_cart_item_1_value())
            self.assert_item_text(MainPage(self.driver).get_item_1_price(), self.get_cart_item_1_price())
            self.click_checkout_button()
            self.get_current_url()
            self.assert_url('https://www.saucedemo.com/checkout-step-one.html')
            Logger.add_end_step(url=self.driver.current_url, method='to_order_item_1')