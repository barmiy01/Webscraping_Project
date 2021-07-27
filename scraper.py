#%% 

from numpy import add
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import pandas as pd
import time


# try:
#     elem = driver.find_element_by_xpath(".//*[@id='SORM_TB_ACTION0']")
#     elem.click()
# except NoSuchElementException:  #spelling error making this code not work as expected
#     pass


URL = f"http://www.matweb.com/search/PropertySearch.aspx/Physical"
driver = webdriver.Chrome('chromedriver')
driver.get(URL)
metal_button = driver.find_element_by_xpath('//*[@id="ctl00_ContentMain_ucMatGroupTree_LODCS1_msTreeViewt3"]')
find_button = driver.find_element_by_xpath('//*[@id="ctl00_ContentMain_btnSubmit"]')
metal_button.click()
find_button.click()

material_features = {'Material_Name':[], 'Atomic_Number':[], 'Electronegativity':[], 'Boiling_Point':[]}
material_list = driver.find_element_by_xpath('//*[@id="tblResults"]/tbody')
material_items = material_list.find_elements_by_class_name('altrow')
hrefs = []

# looping over pages to extract all information
#page = driver.find_element_by_xpath('//*[@id="ctl00_ContentMain_UcSearchResults1_drpPageSelect1"]')
#page_number = page.find_elements_by_tag_name('option')
#print(page_number)

select = Select(driver.find_element_by_xpath('//*[@id="ctl00_ContentMain_UcSearchResults1_drpPageSelect1"]'))
print(select.options)
page_number = [o.text for o in select.options] # these are string-s
for i in page_number:
    select = Select(driver.find_element_by_xpath('//*[@id="ctl00_ContentMain_UcSearchResults1_drpPageSelect1"]'))
    print(select.options)
    select.select_by_visible_text(i)

    material_list = driver.find_element_by_xpath('//*[@id="tblResults"]/tbody')
    material_items = material_list.find_elements_by_class_name('altrow')

    for item in material_items:
            link = item.find_element_by_xpath('.//a').get_attribute('href')
            hrefs.append(link)

    for href in hrefs:
        try:
            driver.get(href)
            material_name = driver.find_element_by_xpath('//*[@id="ctl00_ContentMain_ucDataSheet1_pnlMaterialData"]/table[1]/tbody/tr[1]/th')
            atomic_number = driver.find_element_by_xpath('//*[@id="ctl00_ContentMain_ucDataSheet1_pnlMaterialData"]/table[2]/tbody/tr[16]/td[2]')
            electronegativity = driver.find_element_by_xpath('//*[@id="ctl00_ContentMain_ucDataSheet1_pnlMaterialData"]/table[2]/tbody/tr[23]/td[2]')
            boiling_point =  driver.find_element_by_xpath('//*[@id="ctl00_ContentMain_ucDataSheet1_pnlMaterialData"]/table[2]/tbody/tr[50]/td[2]/a')
            material_features['Material_Name'].append(material_name.text)
            material_features['Atomic_Number'].append(atomic_number.text)
            material_features['Electronegativity'].append(electronegativity.text)
            material_features['Boiling_Point'].append(boiling_point.text)
            time.sleep(1)
        except NoSuchElementException:
            pass

    
    # click the metal hyperlink to go to the first page and then click next page. 
    # This is used since there is no next page button on the page containing info on the property of the materials.
    metal_category_button = driver.find_element_by_xpath('//*[@id="ctl00_ContentMain_ucDataSheet1_trMatlGroups"]/td[2]/a[1]')
    metal_category_button.click()
    #next_page_button = driver.find_element_by_xpath('//*[@id="ctl00_ContentMain_UcSearchResults1_lnkNextPage"]')
    #next_page_button.click()



''' follow this syntax

for href in hrefs:
        driver.get(href)
        price = driver.find_element_by_xpath('//span[@data-testid="price"]').text
        no_bedrooms = driver.find_element_by_xpath('//span[@data-testid="beds-label"]').text
        address = driver.find_element_by_xpath('//span[@data-testid="address-label"]').text
        house_characteristics['Price'].append(price)
        house_characteristics['Address'].append(address)
        house_characteristics['Bedrooms'].append(no_bedrooms)
        time.sleep(1)
'''


# %%
#%%
print(material_features)
# %%
