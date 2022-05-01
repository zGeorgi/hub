from selenium import webdriver

import time

from WD_invoke_browsers.firefox_wd_windoows import FFTests
from explicite_wait import ExplicitWaitType


class ExplicitWaitDemo2:

    def test(self):
        baseUrl = "https://courses.letskodeit.com/"
        wd = FFTests()
        driver = wd.create_wd("chrome")
        driver.implicitly_wait(2)
        driver.maximize_window()
        driver.get(baseUrl)

        wait = ExplicitWaitType(driver)
        element = wait.waitForElement(locator="//a[text()='Sign In']", locatorType="xpath")
        element.click()

        time.sleep(2)
        driver.quit()

ff = ExplicitWaitDemo2()
ff.test()