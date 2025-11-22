from selenium import webdriver
from selenium_stealth import stealth
driver = webdriver.Chrome()

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True)

driver.get("https://www.google.com/")

SEARCH_BOX = driver.find_element("name", "q")
SEARCH_BOX.send_keys("PERSON SELFIE")
SEARCH_BOX.submit()

iframes = driver.find_elements("tag name", "iframe")








































