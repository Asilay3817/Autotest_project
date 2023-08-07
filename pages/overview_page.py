from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from pages.main_page import MainPage
from utilities.logger import Logger


class OverviewPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #locators

    item_1_overview_value = "//div[@class='inventory_item_name']"
    item_1_overview_price = "//div[@class='inventory_item_price']"
    total_price = "//div[@class='summary_subtotal_label']"
    finish_button = "//button[@id='finish']"


    #Getters

    def get_item_1_overview_value(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.item_1_overview_value)))

    def get_item_1_overview_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.item_1_overview_price)))

    def get_total_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.total_price)))

    def get_finish_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.finish_button)))


    #Actions

    def click_finish_button(self):
        self.get_finish_button().click()
        print('Click finish button')


    #Methods

    def finish_order(self):
        with allure.step("Finish order"):
            Logger.add_start_step(method='finish_order')
            self.get_screenshot("overview_page")
            self.assert_item_text(MainPage(self.driver).get_item_1_value(), self.get_item_1_overview_value())
            self.assert_item_text(MainPage(self.driver).get_item_1_price(), self.get_item_1_overview_price())
            self.assert_total_price(MainPage(self.driver).get_item_1_price(), self.get_total_price())
            self.click_finish_button()
            self.get_current_url()
            self.assert_url('https://www.saucedemo.com/checkout-complete.html')
            Logger.add_end_step(url=self.driver.current_url, method='finish_order')