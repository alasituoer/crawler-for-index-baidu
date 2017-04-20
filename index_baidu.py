#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib

driver = webdriver.Chrome()
driver.get('https://index.baidu.com')
elem = driver.find_element_by_id('schword')
elem.send_keys('jingdong')
elem.send_keys(Keys.RETURN)

#alter = driver.switch_to_alert()
elem = driver.find_element_by_id('TANGRAM_12__userName')
elem.send_keys('***')
elem = driver.find_element_by_id('TANGRAM_12__password')
elem.send_keys('***')

driver.find_element_by_id('TANGRAM_12__submit').click()
driver.set_window_size(1200, 900)

for kw in ['京东', '唯品会', '1号店',]:
    kw_re = kw.decode('utf8').encode('gb2312')
    kw_re = urllib.urlencode({'keyword': kw_re}).split('=')[-1]
    url = 'https://index.baidu.com/?tpl=trend&word=' + kw_re
    driver.get(url)

    time.sleep(2) # 隐式等待

    driver.save_screenshot('captures/' + kw + '.png')

time.sleep(2)
driver.close()




