from selenium import webdriver

import time

from selenium.webdriver.common.by import By

from hub.WD_invoke_browsers.firefox_wd_windoows import FFTests
from hub.generic_methods.methods import HandyWrappers


class UsingWrappers1():

    def test(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        wd = FFTests()
        driver = wd.create_wd("chrome")
        driver.implicitly_wait(10)
        driver.get(baseUrl)
        driver.switch_to.frame("courses-iframe")
        element = driver.find_element(By.ID, "search")
        print(element)

        element.send_keys("Java")
        time.sleep(3)


ff = UsingWrappers1()
ff.test()