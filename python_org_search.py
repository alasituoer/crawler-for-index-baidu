#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
assert "百度" in driver.title
elem = driver.find_element_by_id('kw')

time.sleep(3)
elem.clear()
elem.send_keys('pycon')
elem.send_keys(Keys.RETURN)
assert "NO RESULT FOUND." not in driver.page_source
time.sleep(3)
driver.close()
