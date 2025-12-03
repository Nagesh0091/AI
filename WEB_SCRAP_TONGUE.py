from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# SEARCH = PERSON SELFIE WITH TONGUE .jpg files

PHOTOS_WITH_TONGUE = "https://www.google.com/search?sca_esv=e60bbe627df6c182&udm=2&fbs=AIIjpHxU7SXXniUZfeShr2fp4giZ1Y6MJ25_tmWITc7uy4KIeiAkWG4OlBE2zyCTMjPbGmMU8EWskMk2JSE__efdUJ3xRFvZ0M2vJLB0hUMk5HOE2OjlycQYRp9vQECfaBtuI766UjmxPoHIHzqoAp3yNuz3Fl-PVh4hb3ucKWH_IX4pHJi8M0lRnPFaqGQh6DpliW2CemDyaYW9_NLOX7W-LTlOq9fcYw&q=PERSON+SELFIE+WITH+TONGUE+.jpg+files&sa=X&ved=2ahUKEwikx4bF6YeRAxUfTWwGHeDXME0QtKgLegQIFBAB&biw=1536&bih=730&dpr=1.25" 
PHOTOS_WITH_TONGUE_II = "https://www.google.com/search?sca_esv=e60bbe627df6c182&q=glasses+stock+photo+STUDENTS+SELFIE+WITH+TONGUE+.jpeg+files&uds=AOm0WdE2fekQnsyfYEw8JPYozOKz5N4qrBBhXasJuPwyGZfpIZ2OL8_p0Tn1NuH_le3fUs4tl4_qJoTU9g7jWAbQpqr9DecPpe0Jt4EMreKAbO4mwxgzy4PtNZTch7jA7H8wVwZyn41PgZi9eajIF4kLV3m0m1BO02JACOGHjSxST5sZs5puyI1LsRV574atYpewAY4Um3XSQgCvi1qB7d9tzkFT30-WhNK3oryeeI0IGR4AwbL6watctxXQXGV7QOI3-jc09wlY&udm=2&sa=X&ved=2ahUKEwjH0fzipqCRAxW91jgGHZ6rIl4QxKsJKAF6BAgVEAE&ictx=0&biw=1536&bih=730&dpr=1.25"
driver.get(PHOTOS_WITH_TONGUE_II)

time.sleep(2)

# FOR ALL THUMBNAILS THE CLASS IS COMMON(YQ4gaf)

thumbnails = driver.find_elements("xpath","//img[@class='YQ4gaf']")
print(len(thumbnails))

# IF WE DIRECTLY DOWNLOAD THE THUMBNAILS, THE QUALITY OF IMAGE IS VERY LOW. IMAGES ARE NOT CLEAR.
# SO I DECIDED TO DOWNLOAD THE BIG IMAGES BY CLICKING ON THUMBNAILS.
# TO CLICK ON THUMBNAILS, WE HAVE ALREADY GOT THE ELEMENTS OF THUMBNAILS.
# SO NOW IT SHOULD CLICK ON EACH THUMBNAIL AND EXTRACT THE BIG IMAGE URL.

BIG_IMAGE_URL = []

for thumbnail in thumbnails:
    try:
        thumbnail.click()
        time.sleep(1)
    except Exception as e:
        print("Could not click thumbnail:", e)
        continue

    try:
        BIG_IMAGE = driver.find_element("css selector","img.sFlh5c")
        IMAGE_URL = BIG_IMAGE.get_attribute("src")
        print(IMAGE_URL)
        BIG_IMAGE_URL.append(IMAGE_URL)
    except Exception:
        print("UNABLE TO EXTRACT BIG IMAGE URL")

# NOW I GOT THE URL MEANS SRC FOR EACH BIG IMAGE.
# NOW I WILL DOWNLOAD IMAGES USING REQUESTS MODULE.

import requests

# NOW TO SAVE THE IMAGES WE WILL NEED NAMES ALSO 
# FOR THAT I WILL USE FOR LOOP.

for I, URL  in enumerate(BIG_IMAGE_URL):
    FILE_NAME = r"C:\Users\Nagesh Agrawal\OneDrive\Desktop\AI\photos with tongue 2" + f"\img_{I}.jpg"
    response = requests.get(URL)
    with open(FILE_NAME,"wb") as file:
        file.write(response.content)
    time.sleep(1)    

print("IMAGES DOWNLOADED SUCCESSFULLY")


time.sleep(3)

driver.quit()
