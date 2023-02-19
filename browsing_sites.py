import wikipedia

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


wikipedia.set_lang("en")

def contt(query):
    result1 = query
    result2 = wikipedia.summary(result1, sentences=5)
    return result2

def function_wiki(q):
    query = q
    browser = webdriver.Chrome('chromedriver.exe')
    browser.get(url="https://en.wikipedia.org/wiki/" + query)
    while True:
        pass


def function_yout(q):
    query = q
    browser = webdriver.Chrome('chromedriver.exe')
    query.replace(" ", "+")
    browser.get(url="https://www.youtube.com/results?search_query=" + query)
    while True:
        pass


def function_google(q):
    query = q
    browser = webdriver.Chrome('chromedriver.exe')
    query.replace(" ", "+")
    browser.get(url="https://www.google.com/search?q=" + query)
    while True:
        pass