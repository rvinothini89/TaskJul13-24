import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# defining pytest fixture with scope as class and this will be called for each class
# initializing driver here so that this will avoid initializing driver multiple times
@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()
