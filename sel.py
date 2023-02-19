
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#ser = Service(r"C:/Users/Admin/Desktop/clg papers and work/voice_Ass/chromedriver.exe")

class infow():
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service('C:/Users/Admin/.wdm/drivers/chromedriver/win32/110.0.5481/chromedriver.exe'))

    def get_info(self, query):
        self.query=query
        self.driver.get(url="https://www.wikipedia.org")
        search = self.driver.find_element('xpath', '//*[@id="search-form"]')
        search
        # search.click()
        # search.send_keys(query)
        #search.send_keys(query)
        #enter = self.driver.find_element("xpath", '//*[@id="search-form"]/fieldset/button')
        # enter.click()
        while True:
             pass

assist=infow()
assist.get_info("neutron star")
