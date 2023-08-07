from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

from utilities.logger import Logger


class MainPage(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators

    item_1_value = "(//div[@class='inventory_item_name'])[1]"
    item_1_price = "(//div[@class='inventory_item_price'])[1]"
    item_1_add_cart_button = "//button[@id='add-to-cart-sauce-labs-backpack']"
    cart_button = "//a[@class='shopping_cart_link']"

    #Getters

    def get_item_1_value(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.item_1_value)))

    def get_item_1_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.item_1_price)))

    def get_item_1_add_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.item_1_add_cart_button)))

    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))

    #Actions

    def click_item_1_add_cart_button(self):
        self.get_item_1_add_cart_button().click()
        print('Click item 1 add to cart button')

    def click_cart_button(self):
        self.get_cart_button().click()
        print('Click cart button')

    #Methods

    def item_1_add_to_cart(self):
        with allure.step("Item 1 add to cart"):
            Logger.add_start_step(method='item_1_add_to_cart')
            self.click_item_1_add_cart_button()
            self.click_cart_button()
            self.get_current_url()
            self.assert_url('https://www.saucedemo.com/cart.html')
            Logger.add_end_step(url=self.driver.current_url, method='item_1_add_to_cart')