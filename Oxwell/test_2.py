from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time, re
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import *



class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Safari
            # ('/Users/user/Documents/chromedriver')
        # self.driver.implicitly_wait(1)
        self.base_url = "http://127.0.0.1/oxwall/"
        self.driver.get(self.base_url)
        self.wait = WebDriverWait(self.driver, 10)

        # self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get(self.base_url)
        # Login
        # initiate login
        driver.find_element_by_css_selector("span.ow_signin_label").click()
        driver.find_element_by_name("identity").clear()
        driver.find_element_by_name("identity").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("pass")
        driver.find_element_by_name("submit").click()

        # Wait
        self.wait.until_not(visibility_of_element_located((By.ID, "base_cmp_floatbox_ajax_signin"))


        # Add news
        driver.find_element_by_name("status").click()
        driver.find_element_by_name("status").clear()
        driver.find_element_by_name("status").send_keys("New news!")
        driver.find_element_by_name("save").click()

        self.assertEqual("New news!", driver.find_element_by_xpath(
                "//li[contains(@id,'action-feed')]/div/div[2]/div/div[3]").text)
        self.assertEqual("Admin", driver.find_element_by_xpath(
            "//li[contains(@id,'action-feed')]/div/div[2]/div/div[2]/a/b").text)
        #Logout
        ActionChains(driver).move_to_element(driver.find_element_by_link_text("Admin")).perform()
        driver.find_element_by_link_text("Sign Out").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to.alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        pass
        # self.driver.quit()
        # self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()