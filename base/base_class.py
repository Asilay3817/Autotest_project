from selenium.webdriver.common.action_chains import ActionChains
import datetime

class Base():


    def __init__(self, driver):
        self.driver = driver


    """Method get current url page"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"current url {get_url}")


    """Method assert url"""
    def assert_url(self, result):
        value_url = self.driver.current_url
        if value_url != result:
            print("Error - url from open page not equal expected url")


    """Method submit"""
    @staticmethod
    def get_submit(element):
        element.submit()
        print('Submit')

    """Method hover element"""
    def get_move(self, item):
        actions = ActionChains(self.driver)
        actions.move_to_element(item).perform()
        print('Hover element')

    """Method scroll to element"""
    def get_scroll(self, item):
        actions = ActionChains(self.driver)
        actions.move_to_element(item).perform()
        actions.scroll_to_element(item).perform()
        print('Scroll to element')


    """Method assert item text"""
    def assert_item_text(self, value, result):
        if value.text != result.text:
            print("Expected text does not match what is displayed")
            print(f"{value.text} / {result.text}")
        else:
            print("Data verification passed")

    """Method assert total cart price"""
    def assert_total_price(self, value, result):
        if value.text != result.text[12:]:
            print("Expected text does not match what is displayed")
            print(f"{value.text} / {result.text}")
        else:
            print("Data verification passed")

    """Method assert text"""
    def assert_text(self, value, result):
        if value.text != result:
            print("Expected text does not match what is displayed")
            print(f"{value.text} / {result}")
        else:
            print("Data verification passed")


    """Method move slider"""
    def get_move_slider(self, slider, x, y):
        actions = ActionChains(self.driver)
        actions.drag_and_drop_by_offset(slider, x, y).perform()
        print('Move slider')


    """Method get screenshot"""
    def get_screenshot(self, name):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M")
        name_skreenshot = f"{name}-{now_date}.png"
        self.driver.save_screenshot("/Users/asilay/Desktop/study/QA/Autotest_project /screen/" + name_skreenshot)


    """Method scroll page"""
    def get_scroll_page(self, x, y):
        self.driver.execute_script(f"window.scroll({x},{y})")
        print('Scroll page')

    """Method assert select checkbox"""
    @staticmethod
    def get_assert_select_checkbox(element):
        if element.get_attribute("checked") == False:
            print('Сheckbox is not selected, but should')
        else:
            print('Сheckbox is selected')

    """Method assert value in input field"""
    def assert_field_value(self, element, value):
        self.driver.execute_script("alert(arguments[0].value);", element)
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        assert alert_text == value, f"Field value '{alert_text}' does not match expected value '{value}'"

    """Method assert error message displayed"""
    def assert_error_message(self, element):
        assert element.is_displayed(), "Error message not displayed but must"