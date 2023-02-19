
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
def function():
    query='artificial intelligence'
    browser = webdriver.Chrome('chromedriver.exe')
    browser.get(url="https://en.wikipedia.org/wiki/"+query)
    while True:
        pass

function()
