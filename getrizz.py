import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

p = r'PATH\chromedriver.exe' #ADD THE PATH TO THE chromedriver.exe HERE
amount = 2 #SET THE AMOUT OF POEMS YOU NEED
file = open('rizzourses.txt', 'a')

with Chrome(executable_path=p) as driver:
    wait = WebDriverWait(driver,15)
    driver.get("https://www.youtube.com/watch?v=jKM-n5KMTM4")

    for item in range(amount): 
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
        time.sleep(15)

    for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#comment-content"))):
        file.write(comment.text+"\n") 

file.close()
print("++++++DONE+++++++")