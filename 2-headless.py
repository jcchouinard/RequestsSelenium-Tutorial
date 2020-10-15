import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = 'https://www.jcchouinard.com/python-for-seo/' 

options = Options()
options.headless = True
# options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(options=options)

driver.get(url)
time.sleep(3)

driver.quit()