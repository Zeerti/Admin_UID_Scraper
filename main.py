
from selenium.webdriver.common.keys import Keys
from login import get_login_info
import re
from bs4 import BeautifulSoup


parser1 = argparse.ArgumentParser(description="Username for eblvd")
parser1.add_argument("username")
args = parser1.parse_args()


login_url = "https://www.eblvd.com/login/"


# Set values
args.password = getpass("Password: ")
creds = {'Username': args.username, "Password": args.password}

driver = SeleniumDriver()

# login
driver.login(login_url, creds)


# RegEx to find SiteID and GroupID
#.*(.{8}[-].{4}[-].{4}[-].{4}[-].{12})
#re.search(r'.{8}(?:-.{4}){3}-.{12}', s).group(0)
