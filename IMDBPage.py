from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TestLocators.IMDBLocators import locators

# Provided all web page data needed and methods in this class and stored it under TestData folder
# Importing locators here, so the locators can be accessed for these methods
class IMDBPage:
    # below are the data needed for web page input
    url = "https://www.imdb.com/search/name/"
    title = "Advanced name search"
    name = "Macaulay"
    birthyear_start = "1960-01"
    birthyear_end = "1989-12"
    birthday = "08-26"
    topic_input = "New York City"

    # initializing driver and wait and this will be called when object is created for this class in test_IMDBPage
    def __init__(self, url, driver):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, 30)

    # Method for accessing web page and returns title of the webpage
    def webPageAccess(self):
        try:
            print(f"Driver type: {type(self.driver)}")
            self.driver.maximize_window()
            self.driver.get(self.url)
            return self.driver.title
        except TimeoutException as e:
            print(e)

    # Method to scroll down and click on expandall button in web page
    def clickExpandAll(self):
        try:
            # after loading need to scroll down the web page to enter details for fetching results
            self.driver.execute_script("window.scrollBy(0,500)", "")
            # Expanding all controls to enter data
            expand_button = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.expandAll)))
            expand_button.click()
        except TimeoutException as e:
            print(e)

    # Method to pass input for name field using explicit wait conditions
    def nameInput(self):
        try:
            name = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.name_locator)))
            # Passing name value
            name.send_keys(self.name)
            return True
        except TimeoutException as e:
            print(e)

    # Method to pass input for birthyear fields using explicit wait conditions
    def birthyear_range(self):
        try:
            BdateFrom = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.birthdateFrom)))
            BdateTo = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.birthdateTo)))
            BdateFrom.send_keys(self.birthyear_start)
            BdateTo.send_keys(self.birthyear_end)
            return True
        except TimeoutException as e:
            print(e)

    # Method to pass input for birthday field using explicit wait conditions
    def birthday_input(self):
        try:
            Bday = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.birthday)))
            Bday.send_keys(self.birthday)
            return True
        except TimeoutException as e:
            print(e)

    # Method to select award options
    def awardOption_input(self):
        try:
            # need to scroll down further to make the elements visible
            self.driver.execute_script("window.scrollBy(0,800)", "")
            # award options are not clickable with error "not scrolled as its not in view", so tried to execute javascript
            awardOptions = self.driver.find_element(By.XPATH, locators.awards)
            self.driver.execute_script("arguments[0].click();", awardOptions)
            return True
        except TimeoutException as e:
            print(e)

    # Method to select drop down option
    def topicOptionSelect(self):
        try:
            # Tried with select class dint work, so used javascript to select the drop down value
            self.driver.execute_script("return document.getElementById('within-topic-dropdown-id').selectedIndex = '2'")
            # with javascript, it was changing to default option. so tried to trigger the change manually using dispatchEvent method
            self.driver.execute_script("""
                                   var select = document.getElementById('within-topic-dropdown-id');
                                   var event = new Event('change', { bubbles: true });
                                   select.dispatchEvent(event);
                               """)
            return True
        except TimeoutException as e:
            print(e)

    # Method for passing page topic values using explicit wait conditions
    def topicInputText(self):
        try:
            tInput = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.topic_input)))
            tInput.send_keys(self.topic_input)
            return True
        except TimeoutException as e:
            print(e)

    # Method for fetching results by clicking on "See results button" using explicit wait condition
    def resultsClick(self):
        try:
            resultsButton = self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.results)))
            resultsButton.click()
            # Waiting for results to load and taking screenshot to verify the output
            self.wait.until(EC.presence_of_element_located((By.XPATH, locators.results_locator)))
            self.driver.save_screenshot("results.png")
            return True
        except TimeoutException as e:
            print(e)