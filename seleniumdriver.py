from selenium import webdriver


class SeleniumDriver():

    def

    # Connect to URL get HTML
    browser = webdriver.Firefox()
    browser.get(login_url)

    username_login_form = browser.find_element_by_id("Username")
    password_login_form = browser.find_element_by_id("Password")

    username_login_form.clear()
    password_login_form.clear()

    username_login_form.send_keys(values['Username'])
    password_login_form.send_keys(values['Username'])
