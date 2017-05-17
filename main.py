
from selenium.webdriver.common.keys import Keys
from seleniumdriver import SeleniumDriver
import argparse
from getpass import getpass
import re
from bs4 import BeautifulSoup
from eblvd_handler import EblvdHandler
import os

LOGIN_URL = "https://www.eblvd.com/login/"
HOME_URL = "https://www.eblvd.com/hostpcs.aspx"

parser1 = argparse.ArgumentParser(description="Username for eblvd")
parser1.add_argument("username")
args = parser1.parse_args()


# Set values
args.password = getpass("Password: ")
creds = {'Username': args.username, "Password": args.password}

#web_driver = SeleniumDriver()
eblvd_driver = EblvdHandler()

eblvd_driver.connect()



# login to EBLVD
web_driver.login(LOGIN_URL, creds)

# Get all clickable buttons
web_driver.get_clickable_buttons()
#active_buttons = web_driver.find_active_buttons()
#inactive_buttons = web_driver.find_inactive_buttons()

#print("Found {} Active buttons\nFound {} Inactive buttons".format(
#    len(active_buttons), len(inactive_buttons)))



# RegEx to find SiteID and GroupID
#.*(.{8}[-].{4}[-].{4}[-].{4}[-].{12})
#re.search(r'.{8}(?:-.{4}){3}-.{12}', s).group(0)
