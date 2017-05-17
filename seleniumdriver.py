from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SeleniumDriver():

    def __init__(self, *args, **kwargs):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(60)

    def login(self, login_url, creds):

        # Connect to URL get HTML
        self.browser.get(login_url)

        username_login_form = self.browser.find_element_by_id("username")
        password_login_form = self.browser.find_element_by_id("passwordplace")

        # Must be called to clear out default text in forms
        username_login_form.clear()
        password_login_form.clear()

        # input username and password
        username_login_form.send_keys(creds['Username'])
        password_login_form.send_keys(creds['Password'])

        self.browser.find_element_by_id("_signin").click()

        self.browser.find_element_by_xpath("//input[@class='form']").click()
        print(type(self.browser.find_element_by_xpath(
            "//input[@class='form']")))

    def find_active_buttons(self):
        if(self.browser.find_elements_by_xpath("//tr[@class='pcrow']//td[@class='rbtn']//a[@title='Connect to this PC']")[0].get_attribute('innerHTML')):
            time.sleep(2)
            return self.browser.find_elements_by_xpath("//tr[@class='pcrow']//td[@class='rbtn']//a[@title='Connect to this PC']")

        else:
            print('Found nothing')

    def find_inactive_buttons(self):
        if(self.browser.find_elements_by_class_name('connbtn.offline')[0]):
            time.sleep(2)
            return self.browser.find_elements_by_class_name('connbtn.offline')
        else:
            print('Found nothing')

    def pull_html(self):
        return self.browser.page_source

    def get_clickable_buttons(self):

        active_buttons = web_driver.find_active_buttons()
        inactive_buttons = web_driver.find_inactive_buttons()
