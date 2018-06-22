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


class Oxwall:
    def __init__(self, base_url="http://127.0.0.1/oxwall/"):
        self.driver = webdriver.Safari
            # ('/Users/user/Documents/chromedriver')
        # self.driver.implicitly_wait(1)
        self.base_url = "%s" % base_url
        self.driver.get(self.base_url)
        self.wait = WebDriverWait(self.driver, 10)

    def login(self, username="admin", password="pass"):
        # initiate login
        driver = self.driver
        driver.find_element_by_css_selector("span.ow_signin_label").click()
        driver.find_element_by_name("identity").clear()
        driver.find_element_by_name("identity").send_keys("%s" % username)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("%s" % password)
        driver.find_element_by_name("submit").click()
        # Wait login
        self.wait.until_not(visibility_of_element_located((By.ID, "floatbox_overlay")))


    def list_of_news(self):
        return ld_list_of_news = driver.find_elements_by_xpath("//li[contains(@id,'action-feed')]/div/div[2]/div/div[3]")
        # Add new news
        driver.find_element_by_name("status").click()
        driver.find_element_by_name("status").clear()
        driver.find_element_by_name("status").send_keys("!New news!")
        driver.find_element_by_name("save").click()


    def logout(self):
        ActionChains(driver).move_to_element(driver.find_element_by_link_text("Admin")).perform()
        driver.find_element_by_link_text("Sign Out").click()

    def close(self):
        self.driver.quit()