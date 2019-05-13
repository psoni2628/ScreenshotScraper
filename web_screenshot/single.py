from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time

driver = webdriver.Firefox()
delay = 20
pageNum = 0 
pageLimit = 993 

# login
driver.get("" + str(pageNum))
time.sleep(10)
emailElement = driver.find_element_by_id('emailForSignIn')
emailElement.send_keys('')
time.sleep(2)
pwElement = driver.find_element_by_id("passwordForSignIn")
pwElement.send_keys('')
time.sleep(2)
emailElement.send_keys(Keys.ENTER)

time.sleep(5)


while(pageNum <= pageLimit):
    driver.get("https://ereader.chegg.com/#/books/9780190699581/cfi/" + str(pageNum))
    try:
        element = WebDriverWait(driver, delay).until(
            EC.visibility_of_any_elements_located((By.ID, "jigsaw-placeholder-outer"))
        )
    except TimeoutException:
        print("Exception: jigsaw-placeholder-outer not found")
        break
    print("Sleep start")
    time.sleep(5)
    print("Sleep end")
    el = driver.find_element_by_id("jigsaw-placeholder-outer")
    driver.save_screenshot(str(pageNum) + '.png')
    pageNum += 1
driver.quit()