from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import IEDriverManager, EdgeChromiumDriverManager

from webdriver_manager.opera import OperaDriverManager


class FFTests():
    def create_wd(self, browser='chrome'):
        browser = browser.lower()
        if browser == "firefox":
            driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))
            return driver
        elif browser == "chrome":
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            return driver
        elif browser == "edge":
            driver = webdriver.Edge(EdgeChromiumDriverManager().install())
            return driver

    # def test_wd(self):
    #     driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))
    #     driver.get("https://www.gov.uk/")
    #     print(driver.title)
    #
    # def test_wd_chrome(self):
    #     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    #     driver.get("https://www.gov.uk/")
    #     print(driver.title)
    #
    # def test_wd_edge(self):
    #     driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    #     driver.get("https://www.gov.uk/")
    #     print(driver.title)
    #
    # def test_wd_opera(self):
    #     driver = webdriver.Opera(executable_path=OperaDriverManager().install())
    #     driver.get("https://www.gov.uk/")
    #     print(driver.title)






"""
I need to make a method the can choose wich browser to run 
must support multiple choises
"""

