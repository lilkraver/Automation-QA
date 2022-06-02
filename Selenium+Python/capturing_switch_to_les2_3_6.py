from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.execute_script("document.getElementsByTagName('button')[0].classList.remove('trollface');")
    button = browser.find_element(By.CSS_SELECTOR,"button.btn").click()

    browser.switch_to.window(browser.window_handles[1])

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element(By.XPATH,"//*[@id='input_value']")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.XPATH, "//*[@id='answer']").send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR,"button.btn").click()
    time.sleep(5)

finally:
    time.sleep(10)
    browser.quit()    