#pytest --language=es test_items.py    - команда запуска
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_basket_btn(browser):
    browser.get(link)
    time.sleep(30) 
    btn = browser.find_elements(By.CSS_SELECTOR ,".btn.btn-lg.btn-primary.btn-add-to-basket")

    #проверка наличия кнопки корзины
    assert btn, 'btn is absent'
