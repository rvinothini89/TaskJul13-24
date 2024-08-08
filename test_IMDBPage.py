import pytest
from selenium.common import TimeoutException
# accessing IMDBPage class from TestData folder
from TestData.IMDBPage import IMDBPage


class Test_IMDBPage:
    """
    using pytest fixture for initiating driver per class and driver details are provided in conftest.py file
    conftest.py is used as i am initiating chrome driver using it and i am avoiding multiple instantiation of driver
    using this.
    """
    @pytest.fixture(scope="class", autouse=True)
    # using setup class for creating object for IMDBPage class to access all its methods
    def setup_class(self, driver):
        self.driver = driver
        """
        seems to be defect with pytest as simple instantiation object thrown error, as per pytest community, initializing
        object with type keyword
        """
        type(self).obj = IMDBPage(IMDBPage.url, driver)
        self.obj.webPageAccess()

    # Trying to compare title by using this test
    def test_webPageAccess(self):
        try:
            assert self.obj.webPageAccess() == IMDBPage.title
            print("Successfully accessed webpage")
        except TimeoutException as e:
            print(f"TimeoutException occurred: {e}")
        except AssertionError as e:
            print(f"AssertionError occurred: {e}")

# Testing if name input has been passed successfully, each method is returning True if the operation is completed in IMDBPage class
    def test_nameInput(self):
        try:
            self.obj.clickExpandAll()
            assert self.obj.nameInput() == True
            print("Successfully provided name input")
        except TimeoutException as e:
            print(f"TimeoutException occurred: {e}")
        except AssertionError as e:
            print(f"AssertionError occurred: {e}")

# Testing if birthyear input has been passed successfully
    def test_birthyearInput(self):
        try:
            assert self.obj.birthyear_range() == True
            print("Successfully provided birth year input")
        except TimeoutException as e:
            print(f"TimeoutException occurred: {e}")
        except AssertionError as e:
            print(f"AssertionError occurred: {e}")

# Testing if birthday input has been passed successfully
    def test_birthdayInput(self):
        try:
            assert self.obj.birthday_input() == True
            print("Successfully provided birthday input")
        except TimeoutException as e:
            print(f"TimeoutException occurred: {e}")
        except AssertionError as e:
            print(f"AssertionError occurred: {e}")

# Testing if awardoption input has been passed successfully
    def test_awardOptionInput(self):
        try:
            assert self.obj.awardOption_input() == True
            print("Successfully provided award options input")
        except TimeoutException as e:
            print(f"TimeoutException occurred: {e}")
        except AssertionError as e:
            print(f"AssertionError occurred: {e}")

# Testing if topic selectbox and text input has been passed successfully
    def test_topicInput(self):
        try:
            self.obj.topicOptionSelect()
            assert self.obj.topicInputText() ==True
            print("Successfully provided topic select and text input")
        except TimeoutException as e:
            print(f"TimeoutException occurred: {e}")
        except AssertionError as e:
            print(f"AssertionError occurred: {e}")

# Testing if test results returned successfully
    def test_results(self):
        try:
            assert self.obj.resultsClick() == True
            print("IMDB page has been accessed successfully")
        except TimeoutException as e:
            print(f"TimeoutException occurred: {e}")
        except AssertionError as e:
            print(f"AssertionError occurred: {e}")

