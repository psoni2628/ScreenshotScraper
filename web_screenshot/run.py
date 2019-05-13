from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time

driver = webdriver.Edge()
noMoreChap = False
noMoreProb = False
chapNum = 1
probNum = 1
delay = 20
oneMissing = False
oneMissingIndex = 0

while(noMoreChap == False):
    #If probNum are changed to start at a specific point, need to make sure probNum is not reset
    # if(chapNum != 5):
    probNum = 1
    noMoreProb = False
    oneMissing = False
    print(chapNum)
    print(probNum)
    while(noMoreProb == False):
        driver.get("https://" + str(chapNum) + "-problem-" + str(probNum) + "")
        #Try to load the page and find the answer element. If it is not on the page, then either the chapter has run out of problems, or the textbook has run out of chapters
        try:
            element = WebDriverWait(driver, delay).until(
                EC.visibility_of_any_elements_located((By.CLASS_NAME, "answer"))
            )
        except TimeoutException:
            if(oneMissing == True):
                if(abs(oneMissingIndex - probNum) == 1):
                    noMoreProb = True
                else:
                    oneMissing = False
                    probNum += 1
            else:
                oneMissing = True
                oneMissingIndex = probNum
                probNum += 1
            print("Exception")
            #if the first prob does not load, the chapter does not exist
            if(probNum - 1 == 2):
                noMoreChap = True
                print("break")
                break
        else:
            print("Sleep start")
            time.sleep(5)
            print("Sleep end")
            for i in range(1,5):
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight/4*" + str(i) + ");")
                time.sleep(1)
            el = driver.find_element_by_class_name("TBSPlayer TBS_ROOT")
            saveName = (driver.find_element_by_class_name("title")).text
            el.screenshot(saveName + '.png')
            probNum += 1
    chapNum += 1
driver.quit()