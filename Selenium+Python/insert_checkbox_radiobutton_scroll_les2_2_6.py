from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element(By.XPATH,"//*[@id='input_value']")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.XPATH, "//*[@id='answer']").send_keys(y)

    op1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']").click()

    op2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    browser.execute_script('return arguments[0].scrollIntoView(true);', op2)
    op2.click()

    button = browser.find_element(By.CSS_SELECTOR,"button.btn").click()

    time.sleep(5)

finally:
    
    time.sleep(10)
    browser.quit()