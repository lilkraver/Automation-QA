import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#запуск теста для разных языков
def pytest_addopt(parser):
    parser.addoption('--language', action='store', default=None, help="Choose language")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")        #запрос значения параметра, какой язык
    print("\nstart chrome browser for test..")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
