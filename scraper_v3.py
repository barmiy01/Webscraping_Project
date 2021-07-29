#%%

from numpy import add
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
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
    time.sleep(3)
    atomic_no_xpath = '//div[@class="f-15"]'
    element_name_xpath = '//*[@id="Element-Name"]/div[2]/div[1]/p'
    electronegativity_xpath = '//*[@id="Electronegativity"]/div[2]/div[1]/p'
    boiling_point_xpath = '//*[@id="Boiling-Point"]/div[2]/div[1]/p'

    
    atomic_n = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, atomic_no_xpath)))
    element_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, element_name_xpath)))
    electronegativity = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, electronegativity_xpath)))
    boiling_point = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, boiling_point_xpath)))
    element_features['Element_Name'].append(element_name.text)
    element_features['Atomic_Number'].append(atomic_n.text)
    try:
        element_features['Electronegativity'].append(electronegativity.text)
    except TimeoutException():    
        element_features['Electronegativity'].append('NA')
    try:
        element_features['Boiling_Point'].append(boiling_point.text)
    except TimeoutException():    
        element_features['Boiling_Point'].append('NA')
        


        


# %%
#%%
element_data = pd.DataFrame(element_features)
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(element_data)

# %%
