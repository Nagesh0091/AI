from selenium import webdriver
driver = webdriver.Chrome()

driver.get("https://www.google.com/")

SEARCH_BOX = driver.find_element("name", "q")
SEARCH_BOX.send_keys("PERSON SELFIE")
from selenium.webdriver.common.keys import Keys
SEARCH_BOX.send_keys(Keys.RETURN)

from bs4 import BeautifulSoup
HTML_DATA = BeautifulSoup(driver.page_source, "html.parser")
IFRAMES = HTML_DATA.find_all("iframe") 
print(IFRAMES)

for iframe in IFRAMES:
    src = iframe.get("src")
    if src and "recaptcha" in src:
        # Print the iframe src
        print("reCAPTCHA iframe src:", src)
        # Extract sitekey value from src
        import re
        match = re.search(r'k=([^&]+)', src)
        if match:
            sitekey = match.group(1)
            print("reCAPTCHA sitekey:", sitekey)
            break


# pip install 2captcha-python
import twocaptcha
from twocaptcha import TwoCaptcha


while True:
    pass







































