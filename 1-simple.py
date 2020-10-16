#!/usr/bin/env python
'''
Simple Selenium browser automation.

@author:    Jean-Christophe Chouinard. 
@role:      Sr. SEO Specialist at SEEK.com.au
@website:   jcchouinard.com
@LinkedIn:  linkedin.com/in/jeanchristophechouinard/ 
@Twitter:   twitter.com/@ChouinardJC

What it does:
Opens Chrome;
Visit URL;
Print the HTML of the page;
Close browser.
'''
import time

from selenium import webdriver

url = 'https://www.jcchouinard.com/python-for-seo/' # Define page to run 
driver = webdriver.Chrome() # Open Chrome
driver.get(url)             # Visit URL

print(driver.page_source)   # Print HTML
time.sleep(3)               # Wait 3 Seconds
driver.quit()               # Close browser