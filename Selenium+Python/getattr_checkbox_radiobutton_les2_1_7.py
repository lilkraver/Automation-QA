from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    box = browser.find_element(By.ID, "treasure")
    x = box.get_attribute("valuex")
    y = calc(x)

    input1 = browser.find_element(By.XPATH, "//*[@id='answer']").send_keys(y)

    op1 = browser.find_element(By.ID, "robotCheckbox").click()
    op2 = browser.find_element(By.ID, "robotsRule").click()

    button = browser.find_element(By.CSS_SELECTOR,"button.btn").click()
    time.sleep(5)

finally:
    
    time.sleep(10)
    browser.quit()