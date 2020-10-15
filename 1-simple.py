import time

from selenium import webdriver

url = 'https://www.jcchouinard.com/python-for-seo/' # Define page to run 
driver = webdriver.Chrome() # Open Chrome
driver.get(url)             # Visit URL

print(driver.page_source)   # Print HTML
time.sleep(3)               # Wait 3 Seconds
driver.quit()               # Close browser