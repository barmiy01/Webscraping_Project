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
hrefs = []

for item in element_list[0:103]:
    link = item.find_element_by_xpath('.//a').get_attribute('href')
    hrefs.append(link)

for href in hrefs:
    driver.get(href)
        
    element_name = driver.find_element_by_xpath('//*[@id="Element-Name"]/div[2]/div[1]/p')
    atomic_number = driver.find_element_by_xpath('//*[@id="main-content"]/div/div/div/div[5]/table/tbody/tr[1]/td[3]/div/div/div[1]/div[1]')
    electronegativity = driver.find_element_by_xpath('//*[@id="Electronegativity"]/div[2]/div[1]/p')
    boiling_point = driver.find_element_by_xpath('//*[@id="Boiling-Point"]/div[2]/div[1]/p')
    element_features['Element_Name'].append(element_name.text)
    element_features['Atomic_Number'].append(atomic_number.text)
    element_features['Electronegativity'].append(electronegativity.text)
    element_features['Boiling_Point'].append(boiling_point.text)
    time.sleep(5)

# %%
