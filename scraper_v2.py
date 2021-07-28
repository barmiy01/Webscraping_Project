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

element_features = {'Element_Name':[], 'Atomic_Number':[], 'Electronegativity':[], 'Boiling_Point':[]}

element_list = driver.find_elements_by_xpath("//li[@class='p-md-bottom print-avoid-break-inside print-padding-top']")

for item in element_list[0:103]:
    element_name = item.find_element_by_xpath(".//div[@class='f-125 f-lh-15']")
    atomic_number = item.find_element_by_xpath(".//div[@class='f-1 f-lh-15']")
    electronegativity = item.find_elements_by_xpath(".//span[@class='capitalized']")[3]
    boiling_point =  item.find_element_by_xpath('')
    element_features['Element_Name'].append(element_name.text)
    element_features['Atomic_Number'].append(atomic_number.text)
    element_features['Electronegativity'].append(electronegativity.text)
    element_features['Boiling_Point'].append(boiling_point.text)

# %%
#%%
element_data = pd.DataFrame(element_features)
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(element_data)
# %%
