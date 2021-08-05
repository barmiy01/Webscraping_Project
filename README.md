# Webscraping Project

## Predicting the Band Gap of Compounds using Elemental Descriptors

## Abstract

It has been shown that there is a predictive relationship
between 'known discrete scalar descriptors associated with crystal and electronic structure and observed properties of materials'.
However, the property space of these materials is of high dimensionality which highlights the complex nature of predictive models at the fundamental level. Additionally, the elemental descriptors at this level have a certain degree of co-dependence which makes prediction even more complicated. It has been demonstrated using data reduction methods that the property space of observable material properties can be diminished.  In this project, a dataset of elements and some of their corresponding elemental descriptors have been collected using webscraping techniques. The elemental descriptors/features were limited to five since it has been shown that it is possible to predict band gap energies using only five (5) elemental descriptors.

## Motivation

Recent advances in material science and engineering have been focused on 
producing rational design rules and principles for material fabrication.
The development of these design rules have huge implications for various fields such as crystal engineering, opto-electronics and photonics . In this regard, considerable attempts have been made to utilize already accumulated datasets to create models that facilitate the prediction of various material properties using machine learning techniques. Despite recent advances in this field, there is a dearth of machine-learning-based models to predict band gap energies.

## Methodology

Implementing python libraries such as selenium and pandas, a database of elements with elemental descriptors have been extracted. The code was written to function in a multifaceted way as detailed below:

* Open the desired website containing information on the elements or compound.

* Extract specific information on the attributes of the element or compound.
    * To do this, the python codes ```OQMD_Database_scraper.py``` and ```periodic_table.py``` utilized. These codes contain the functions ```get_elements()``` and ```get_compounds(n)```  that carry out the extraction of elements and compounds data respectively.
    * Specifically, ```get_compounds(n)``` depends on the parameter `n` which is
            an integer that defines the number of pages to extract data from.

* Convert the result into a dataframe for further processing
        * Using Pandas, the extracted data was stored as a data frame using the ```convert_to_DF()``` function which was saved as a csv file.

* Clean the data

    * For the extracted elements data, the boiling point of       elements was extracted in both &deg;C and Kelvin(K) with the boiling point in &deg;C within parentheses. For consistency, we delete all values in parentheses leaving values in K. To do this, we import the module ```regex``` and implement the following code :

         ```re.sub(r'\([^)]*\)', '', '[filename]')``` 

* Import as an SQL database
    * Implementing the python modules ```psycopg2``` and ```SQLAlchemy``` , the output data was imported to SQL in     tabular form. 

Specifically, the main python library used for the extraction of data was selenium. Pandas was used to convert the raw data into a desired output (i.e. a csv file).

## Setting up venv

* Using anaconda3 set up a virtual environment (venv) while meeting necessary code requirements. All necessary requirments can be found in the file ```requirements.txt```.

    ```source activate [env name]```

    ```pip install requirements.txt```

## Running the Project

1. Run the python code that extracts data from OQMD

     ```$ python  OQMD_Database_scraper.py```

2. Run the code that extracts data from the periodic table

    ```$ python periodic_table.py```

3. The entire code be ran from the executable shell script file

    ```$ sh execute.sh```











