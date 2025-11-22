from selenium import webdriver
driver = webdriver.Chrome()

driver.get("https://www.google.com/")

SEARCH_BOX = driver.find_element("name", "q")

from selenium.webdriver.common.keys import Keys
SEARCH_BOX.send_keys("PERSON SELFIE", Keys.RETURN)

import time
time.sleep(3)

from bs4 import BeautifulSoup
HTML_DATA = BeautifulSoup(driver.page_source, "html.parser")
IFRAMES = HTML_DATA.find_all("iframe") 
print(IFRAMES)


for IFRAME in IFRAMES:
    SRC = IFRAME.get("src") # link.
    if SRC is not None and "recaptcha" in SRC:
        print("reCAPTCHA iframe scr:", SRC)
        from urllib.parse import urlparse, parse_qs
        parsed_url = urlparse(SRC)
        params = parse_qs(parsed_url.query)
        sitekey = params.get("k", [None])[0]
        print("reCAPTCHA sitekey from scr:", sitekey)
        break


page_url = driver.current_url
print("Page URL:", page_url)
print("Sitekey:", sitekey)

# pip install 2captcha-python
import twocaptcha
from twocaptcha import TwoCaptcha

import tomllib
with open("config.toml", "rb") as f:
    config = tomllib.load(f)
API_KEY = config["captcha"]["api_key"]

solver = TwoCaptcha(API_KEY) 
result = solver.recaptcha(sitekey=sitekey, url=page_url, enterprise=1)
token = result['code']
print("2captcha token:", token)

driver.execute_script('document.getElementById("g-recaptcha-response").style.display = "block";')
driver.execute_script(f'document.getElementById("g-recaptcha-response").value = "{token}";')

driver.find_element("id", "submit_button_id").click()
# NOW I GOT TO KNOW THAT THAT IS PAID SERVICE.😂😂
# I WILL SOLVE CAPTCHA MANUALLY.

while True:
    pass







































