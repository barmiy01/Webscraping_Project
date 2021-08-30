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
from data_structure import convert_to_DF 
import time
from generic_scraper import Scraper

class PeriodicTableScraper(Scraper):
    '''
    [insert Description]

    Parameters
    ---------
    n : int
    root : str
    list : list
    features: dict

    Attributes
    ----------
    n
    root
    list
    features

    '''
    def __init__(self, **kwargs):
         super().__init__(**kwargs)

    def extract_links(self):
        '''
        Extracts all urls to specific element webpage 
        and stores them in a list.

        '''
        print(f" --- Extracting elemental URLs ---")
        
        self.driver.get(root)
        element_list = self.driver.find_elements_by_xpath("//li[@class='p-md-bottom print-avoid-break-inside print-padding-top']")
        for item in element_list[0:self.n]:
                link = item.find_element_by_xpath('.//a').get_attribute('href')
                self.list.append(link)
        
        print(f"... Done")


    def extract_data(self):
        '''
        For every extracted link in the list, 
        this function extracts the necessary data
        as specified in the parameter 'features'.

        '''
        
        self.extract_links()
        for i in self.list:
            self.driver.get(i)
            time.sleep(3)
            atomic_no_xpath = '//div[@class="f-15"]'
            element_name_xpath = '//*[@id="Element-Name"]/div[2]/div[1]/p'
            electronegativity_xpath = '//*[@id="Electronegativity"]/div[2]/div[1]/p'
            boiling_point_xpath = '//*[@id="Boiling-Point"]/div[2]/div[1]/p'

            try:
                atomic_n = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, atomic_no_xpath)))
                element_name = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, element_name_xpath)))
                electronegativity = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, electronegativity_xpath)))
                boiling_point = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, boiling_point_xpath)))
                self.features['Element_Name'].append(element_name.text)
                self.features['Atomic_Number'].append(atomic_n.text)
                self.features['Boiling_Point'].append(boiling_point.text)
                self.features['Electronegativity'].append(electronegativity.text)
            except TimeoutException: 
                self.features['Electronegativity'].append('NA')
                self.features['Boiling_Point'].append('NA')
        print(f"--- Extracting elemental features ---")
        print(f" ... Done")
        # if to_DF == True:
        #     print(f"converting to DF ...")
        #     convert_to_DF(self.element_features, 'elements_data', to_csv=True)
        # else:
        #     pass


if __name__ == '__main__':
    root = "https://pubchem.ncbi.nlm.nih.gov/periodic-table/#view=list"
    features = {'Element_Name':[], 'Atomic_Number':[], 'Electronegativity':[], 'Boiling_Point':[]}
    scraper = PeriodicTableScraper(n=5, root=root, list=[], features=features)
    scraper.extract_data()






# %%
