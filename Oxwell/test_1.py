from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome('/Users/user/Documents/chromedriver')
driver.get("http://127.0.0.1/oxwall/")

driver.implicitly_wait(10)

sign_in = driver.find_element_by_class_name("ow_signin_label")
sign_in.click()

login = driver.find_element_by_name("identity")
login.click()
login.send_keys("admin")

password = driver.find_element_by_name("password")
password.click()
password.send_keys("pass")

accept_button = driver.find_element_by_name("submit")
accept_button.click()

text_area = driver.find_element_by_class_name("ow_newsfeed_status_input")
text_area.click()

text_area.send_keys("My new post.")

save = driver.find_element_by_name("save")
save.click()

logout_button = driver.find_element_by_class_name("ow_console_item_link")
menu = webdriver.ActionChains(driver).move_to_element("ow_console_item_link")

submenu = menu.find_element_by_class_name("ow_console_item_link")[6]
submenu.click()

driver.quit()