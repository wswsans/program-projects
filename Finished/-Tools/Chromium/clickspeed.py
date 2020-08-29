import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import chromedriver_binary

website = 'https://www.arealme.com/click-speed-test/ja/'

chrome_options = webdriver.ChromeOptions();
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
driver = webdriver.Chrome(options=chrome_options);
#driver = webdriver.Chrome('/Users/rockmankun/Selenium/chromedriver')
driver.get(website)

driver.maximize_window()

driver.find_element_by_id('start').click()
doc = driver.find_element_by_id('clickarena')

while True:
    doc.click()
