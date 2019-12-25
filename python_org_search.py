from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.google.com")
elem = driver.find_element_by_name("q")
elem.send_keys("freemail")
elem.send_keys(Keys.RETURN)
elem = driver.find_element_by_class_name("iUh30").click()
elem = driver.find_element_by_id ("id-l")
elem.send_keys("imbox@ukr.net")
elem = driver.find_element_by_id ("id-p")
elem.send_keys("000000000")
elem = driver.find_element_by_class_name("button.button_style-main.button_size-regular.form__submit").click()
