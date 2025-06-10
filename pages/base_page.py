import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.locators_base_page import LocatorsBasePage

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_url(self, url):
        self.driver.get(url)

    def find_of_element(self, locator):
        self.driver.find_element(*locator)

    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    def send_keys_to_input(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys)

    def add_text_to_element(self, locator, text):  
        self.find_of_element_whith_wait(locator).send_keys(text)

    def scrolling_to_element(self, locator):
        element = self.wait_visibility_of_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_visibility_of_element(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))

    def get_text(self, locator):
        return self.driver.find_element(*locator).text
    
    def get_text_from_element(self, locator): 
        return self.find_of_element_whith_wait(*locator).text

    def get_tab_and_switch(self):
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])
        return tabs

    def check_switch_dzen(self):
        return WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(LocatorsBasePage.yandex))
    