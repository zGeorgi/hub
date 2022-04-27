from selenium import webdriver

import time

from WD_invoke_browsers.firefox_wd_windoows import FFTests
from generic_methods.methods import HandyWrappers


class UsingWrappers1():

    def test(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        wd = FFTests()
        driver = wd.create_wd("firefox")
        driver.maximize_window()
        driver.implicitly_wait(10)
        hw = HandyWrappers(driver)
        driver.get(baseUrl)

        textField1 = hw.getElement("name")
        textField1.send_keys("Test")
        time.sleep(2)
        textField2 = hw.getElement("//input[@id='name']", locatorType="xpath")
        textField2.clear()

ff = UsingWrappers1()
ff.test()