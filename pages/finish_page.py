from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class FinishPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #locators

    complete_header = "//h2[@class='complete-header']"
    back_home_button = "//button[@id='back-to-products']"



    #Getters

    def get_complete_header(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.complete_header)))

    def get_back_home_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.back_home_button)))


    #Actions

    def click_back_home_button(self):
        self.get_back_home_button().click()
        print('Click home button')


    #Methods

    def back_home(self):
        self.get_screenshot("finish_page")
        self.assert_text(self.get_complete_header(), "Thank you for your order!")
        self.click_back_home_button()
        self.get_current_url()
        self.assert_url('https://www.saucedemo.com/inventory.html')