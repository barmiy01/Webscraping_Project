#%%
from numpy import add
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait

# chromeOptions = webdriver.ChromeOptions()
# chromeOptions.add_argument("--no-sandbox") 
# chromeOptions.add_argument("--disable-setuid-sandbox") 
# chromeOptions.add_argument("--disable-dev-shm-using") 
# chromeOptions.add_argument("--disable-extensions") 
# chromeOptions.add_argument("--disable-gpu") 
# chromeOptions.add_argument("start-maximized") 
# chromeOptions.add_argument("disable-infobars") 
# chromeOptions.add_argument("--headless") 

class Scraper:
    def __init__(self, **kwargs):
        self.n = kwargs['n']
        self.root = kwargs['root']
        self.list = kwargs['list']
        self.features = kwargs['features']
        self.driver = webdriver.Chrome('chromedriver')

# %%
