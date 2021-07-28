#%%
from numpy import add
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

URL = f"https://pubchem.ncbi.nlm.nih.gov/periodic-table/#view=list"
driver = webdriver.Chrome('chromedriver')
driver.get(URL)

element_features = {'Name':[], 'Spacegroup':[], 'Volume':[], 'Band_gap':[]}

element_list = driver.find_elements_by_xpath("//*[@class='clickableRow']")


# %%
#%%
print(element_list)
# %%
