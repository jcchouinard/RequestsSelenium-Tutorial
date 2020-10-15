import time

from reppy.robots import Robots
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from functions import get_domain_name

domain = 'https://www.jcchouinard.com/'
uris = ['python-for-seo','wp-content']
urls = [domain + uri for uri in uris] # combine domain to URL

def get_robots_url(url):
    '''
    Convert URL to get the /robots.txt url
    '''
    domain_url = get_domain_name(url)
    robots_url = domain_url + '/robots.txt'
    return robots_url

def robot_parser(url):
    '''
    Parse the Robots.txt.
    Send True if it is allowed to crawl
    '''
    robotstxt = get_robots_url(url)
    parser = Robots.fetch(robotstxt)
    validation = parser.allowed(url, '*')
    return validation

def print_title(url,headless=True):
    '''
    Run Selenium.
    Print Title.
    '''
    print(f'Opening {url}')
    options = Options()
    options.headless = headless
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    t = driver.title
    print(f'Title: {t}')
    driver.quit()

def run_selenium(url):
    '''
    Check if robots.txt allows.
    If it does, run print_title()
    Else. Tell the user it is blocked
    '''
    validation = robot_parser(url)
    if validation:
        print_title(url)
    else:
        print(f'{url} is blocked by robots.txt')

for url in urls:
    run_selenium(url)
print('Done')
    