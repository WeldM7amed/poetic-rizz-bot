import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

file = open('rizzourses.txt', 'a')
p=r'C:\Users\Ben Yedder\Downloads\chromedriver_win32\chromedriver.exe'

with Chrome(executable_path=p) as driver:
    wait = WebDriverWait(driver,15)
    driver.get("https://www.youtube.com/watch?v=jKM-n5KMTM4")

    for item in range(2): 
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
        time.sleep(15)

    for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#comment-content"))):
        file.write(comment.text+"\n") 

file.close()