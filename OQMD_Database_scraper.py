#%%
from numpy import add
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from sqlalchemy import create_engine
import pandas as pd
import time

def get_compounds(n=2):

    '''
    Extracts information on the attributes of materials
    where these features are:

    Features
    --------
    (1) Name
    (2) Spacegroup
    (3) Volume
    (4) Band Gap

    Parameter
    ---------
    n : int
        Defines the number of pages to extract data from

    '''

    URL = f"http://oqmd.org/api/search#apisearchresult"
    driver = webdriver.Chrome('chromedriver')
    driver.get(URL)

    compound_features = {'Name':[], 'Spacegroup':[], 'Volume':[], 'Band_gap':[]}

    search_button = driver.find_element_by_xpath('//*[@id="submit-id-search"]')
    search_button.click()

    table = driver.find_element_by_xpath('//*[@id="ResultTable"]/tbody')
    compound_list = table.find_elements_by_xpath('.//tr')[1:]
    
    for _ in range(n):
        
        next_page_button = driver.find_element_by_xpath('//button[@class="next"]')
        #redefined due to the staleElement error
        table = driver.find_element_by_xpath('//*[@id="ResultTable"]/tbody')
        compound_list = table.find_elements_by_xpath('.//tr')[1:]
        
        for item in compound_list:
            name = item.find_element_by_xpath('.//td[@width="60"]')
            spacegroup = item.find_elements_by_xpath('.//td[@width="50"]')[3]
            volume = item.find_elements_by_xpath('.//td[@width="80"]')[1]
            band_gap = item.find_elements_by_xpath('.//td[@width="50"]')[5]
            compound_features['Name'].append(name.text)
            compound_features['Spacegroup'].append(spacegroup.text)
            compound_features['Volume'].append(volume.text)
            compound_features['Band_gap'].append(band_gap.text)
            time.sleep(1)
        
        next_page_button.click()
        time.sleep(10)
    driver.close()
    return compound_features

def convert_to_DF(name='raw_compound_features'):
    '''
    Stores the extracted data as a data frame

    Parameter
    ---------
    name : str
           Defines the name of the variable storing the extracted data from get_compounds()

    '''
    name = get_compounds()
    compounds_data = pd.DataFrame(name)
    with pd.option_context('display.max_rows', None, 'display.max_columns', None): 
        return compounds_data

def import_to_SQL(name='compounds_dataset'):
    '''
    Imports the output as an SQL database

    '''
    DATABASE_TYPE = 'postgresql'
    DBAPI = 'psycopg2'
    HOST = 'localhost'
    USER = 'postgres'
    PASSWORD = 'kenya123'
    DATABASE = 'Compounds_databse'
    PORT = 5432
    engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")

    compounds_data.to_sql(name, engine, if_exists='replace')




compounds_data = convert_to_DF()

#%%
import_to_SQL()










# %%
