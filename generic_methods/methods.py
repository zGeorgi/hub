
from traceback import print_stack

from selenium.common.exceptions import NoSuchElementException, ElementNotSelectableException, ElementNotVisibleException

from datetime import time


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HandyWrappers:

    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = str(locatorType.lower())

        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "classname":
            return By.CLASS_NAME
        elif locatorType == "linktext":
            return By.LINK_TEXT
        else:
            print("Locator type " + locatorType + " not correct/supported")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            print("Element Found")
        except:
            print("Element not found")
        return element


    def element_presence_check(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                print("Element Found")
                return True
            else:
                print("Element not found")
                return False
        except:
            print("Element not found")
            return False

    def is_element_present(self, locator, byType):
        try:
            element = self.driver.find_element(byType, locator)
            if element is not None:
                print("Element Found")
                return True
            else:
                print("Element not found")
                return False
        except:
            print("Element not found")
            return False

    def dynamic_xpath(self, xpat, text):
        xpat = xpat
        text = text
        #//form[@id='search' and @name='{0}']
        # "//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]"
        raw = xpat
        ready_xpath = raw.format(text)
        return ready_xpath


    def take_screenshot(self, driver):
        """
        Takes screenshot of the current open web page
        :param driver
        :return:
        """
        fileName = str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "/Users/atomar/desktop/"
        destinationFile = screenshotDirectory + fileName

        try:
            driver.save_screenshot(destinationFile)
            print("Screenshot saved to directory --> :: " + destinationFile)
        except NotADirectoryError:
            print("Not a directory issue")



def waitForElement(self, locator, locatorType="id",
                   timeout=10, pollFrequency=0.5):
    element = None
    try:
        self.driver.implicitly_wait(0)
        byType = self.getByType(locatorType)
        print("Waiting for maximum :: " + str(timeout) +
              " :: seconds for element to be visible")
        wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=pollFrequency,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        element = wait.until(EC.visibility_of_element_located((byType, locator)))
        print("Element appeared on the web page")
    except:
        print("Element not appeared on the web page")
        print_stack()
    self.driver.implicitly_wait(2)
    return element