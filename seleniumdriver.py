from selenium import webdriver
from selenium.webdriver.common.by import By

class SeleniumDriver():

    def __init__(self, *args, **kwargs):
        self.browser = webdriver.Firefox()

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

    def pull_html(self):
        return self.browser.page_source
        