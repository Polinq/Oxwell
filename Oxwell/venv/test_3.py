from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import *
import unittest, time, re
from oxwall_expected_condition import amount_of_elements_located
from oxwall_application import Oxwall

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Oxwall()


    def test_untitled_test_case(self):
        self.app.login('admin', 'pass')


        old_list_of_news = driver.find_elements_by_xpath("//li[contains(@id,'action-feed')]/div/div[2]/div/div[3]")

     def add_new_news(self):
        # Add new news
        driver = self.driver
        driver.find_element_by_name("status").click()
        driver.find_element_by_name("status").clear()
        driver.find_element_by_name("status").send_keys("!New news!")
        driver.find_element_by_name("save").click()

        #  Wait for new news to appear
        self.wait.until(
            amount_of_elements_located((By.XPATH, "//li[contains(@id,'action-feed')]/div/div[2]/div/div[3]"),
                                       len(old_list_of_news) + 1))
        # Verify
        self.assertEqual("!New news!", driver.find_element_by_xpath(
            "//li[contains(@id,'action-feed')]/div/div[2]/div/div[3]").text)
        self.assertEqual("Admin", driver.find_element_by_xpath(
            "//li[contains(@id,'action-feed')]/div/div[2]/div/div[2]/a/b").text)
        # Logout
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
        self.app.close()
        # self.app.driver.quit()


if __name__ == "__main__":
    unittest.main()