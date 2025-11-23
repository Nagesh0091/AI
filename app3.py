from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import os
import requests
import shutil

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com/")
SEARCH_BOX = driver.find_element(By.NAME, "q")
SEARCH_BOX.send_keys("PERSON SELFIE .jpg files", Keys.RETURN)

time.sleep(60)

HTML_DATA = BeautifulSoup(driver.page_source,"html.parser")
TAB = HTML_DATA.find_all("span",class_="R1QWuf")
clickable_elements = driver.find_elements(By.CSS_SELECTOR, "span.R1QWuf")

if len(clickable_elements) >= 3:
    clickable_elements[2].click()

time.sleep(3)

thumbnails = driver.find_elements(By.XPATH, "//img[@class='YQ4gaf']")

count = 1
URL = []

for thumb in thumbnails:
    driver.execute_script("arguments[0].scrollIntoView();", thumb)
    time.sleep(1)
    try:
        thumb.click()
        time.sleep(1)
    except Exception:
        driver.execute_script("arguments[0].click();", thumb)
        time.sleep(1)
    try:
        big_img = driver.find_element(By.CSS_SELECTOR, "img.sFlh5c")
        img_url = big_img.get_attribute("src")
        URL.append(img_url)
        count += 1
    except Exception:
        count += 1
        continue

import os
import requests
import shutil

folder = r"C:\Users\Nagesh Agrawal\OneDrive\Desktop\AI\photos"
os.makedirs(folder, exist_ok=True)

for i, url in enumerate(URL):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        ext = "jpg"
        file_path = os.path.join(folder, f"img_{i}.{ext}")

        with open(file_path, "wb") as f:
            shutil.copyfileobj(response.raw, f)

        print("Downloaded:", file_path)

    except Exception as e:
        print("Failed:", e)

