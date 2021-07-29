#%%
from numpy import add
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

URL = f"http://oqmd.org/api/search#apisearchresult"
driver = webdriver.Chrome('chromedriver')
driver.get(URL)

element_features = {'Name':[], 'Spacegroup':[], 'Volume':[], 'Band_gap':[]}

search_button = driver.find_element_by_xpath('//*[@id="submit-id-search"]')
search_button.click()

table = driver.find_element_by_xpath('//*[@id="ResultTable"]/tbody')
element_list = table.find_elements_by_xpath('.//tr')[1:]
for _ in range(20):
    next_page_button = driver.find_element_by_xpath('//button[@class="next"]')
    #redefined due to the staleElement error
    table = driver.find_element_by_xpath('//*[@id="ResultTable"]/tbody')
    element_list = table.find_elements_by_xpath('.//tr')[1:]
    
    for item in element_list:
        name = item.find_element_by_xpath('.//td[@width="60"]')
        spacegroup = item.find_elements_by_xpath('.//td[@width="50"]')[3]
        volume = item.find_element_by_xpath('.//td[@width="80"]')
        band_gap = item.find_elements_by_xpath('.//td[@width="50"]')[5]
        element_features['Name'].append(name.text)
        element_features['Spacegroup'].append(spacegroup.text)
        element_features['Volume'].append(volume.text)
        element_features['Band_gap'].append(band_gap.text)
        time.sleep(1)
    
    next_page_button.click()
    time.sleep(10)

# %%
#%%
element_data = pd.DataFrame(element_features)
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(element_data)
# %%
