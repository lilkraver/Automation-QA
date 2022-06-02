from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH, "//input[@class='form-control first' and @required]")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, "//input[@class='form-control second' and @required]")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, "//input[@class='form-control third' and @required]")
    input3.send_keys("Smolensk@num.su")

    button = browser.find_element(By.CSS_SELECTOR,"button.btn").click()

    time.sleep(5)

    welcome_text_elt = browser.find_element(By.TAG_NAME,"h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
