import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function") 
def browser():                          #открыть браузер, ждать, после выполнения закрыть
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()

#изменяемый номер в ссылках
@pytest.mark.parametrize('numb', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, numb):
    answer = str(math.log(int(time.time())))        #ответ для вставки в текстовое поле

    link = f"https://stepik.org/lesson/{numb}/step/1"
    browser.get(link)
    
    input1 = browser.find_element(By.TAG_NAME, "textarea").send_keys(answer)

    button = browser.find_element(By.CLASS_NAME,"submit-submission").click()

    browser.implicitly_wait(10)

    output = browser.find_element(By.CLASS_NAME, "smart-hints__hint").text #найти поле вывода ответа
    
    assert "Correct!" == output  #проверить, что это "Correct!"

if __name__ == "__main__":
    pytest.main()