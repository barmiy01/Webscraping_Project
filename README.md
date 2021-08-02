# Webscraping Project

## Predicting the Band Gap of Compounds using Elemental Descriptors


## Abstract

It has been shown literature that there is a predictive relationship
between known discrete scalar descriptors associated with crystal and electronic structure and observed properties of materials.
However, the property space of these materials is of high dimensionality which highlights the complex nature of predictive models at the fundamental level. Additionally, the elemental descriptors at this level have a certain degree of co-dependence which makes prediction even more complicated. A possible way to address is by using data reduction methods which reduces the dimensionality of the property space. In this project, a dataset of elements and some of their corresponding elemental descriptors have been collected using webscraping techniques. The elemental descriptors/features were limited to five since it has been shown that it is possible to predict band gap energies using only five (5) elemental descriptors.




## Motivation

Recent advances in material science and engineering have been focused on 
producing rational design rules and principles for material fabrication.
The development of these design rules have huge implications for various such as fields opto-electronics, photonics [add more examples] etc. In this regard, considerable attempts have been made to utilize already accumulated datasets to create models that facilitate the prediction of various material properties using machine learning techniques. Despite the growing interests in predictive models using machine learning, there is a dearth of machine-learning-based models to predict band gap energies. 

## Methodology

Implementing python libraries such as selenium and pandas, a database of elements with elemental descriptors have been extracted. The code was written to function in a multifaceted way as detailed below:

* Open the desired website containing information on the elements or compound.

* Extract specific information on the attributes of the element or compound.
    * To do this, the functions *get_elements()* and *get_compounds()* were utilized to extract elements and compounds data respectively.
    * Specifically, *get_compounds()* depends on the parameter *n* which is
    an integer that defines the number of pages to extract data from.

* Convert the result into a dataframe for further processing
    * Using Pandas, the extracted data was stored as a data frame using the *convert_to_DF()* function which was saved as a csv file.

* Clean the data

* Import as an SQL database

Specifically, the main python library used for the extraction of data was selenium. Pandas was used to convert the raw data into a desired output (i.e. a csv file).

## Setting up venv

* Using anaconda3 set up a virtual environment (venv) while meeting necessary code requirements. All necessary requirments can be found in the file ```requirements.txt```.

    ```source activate [env name]```

    ```pip install requirements.txt```

## Running the Project

1. Run the python code that extracts data from OQMD

     ```$ python  OQMD_Database_scraper.py```

2. Run the code that extracts data from the periodic table

    ```$ python scraper_v3.py```

3. The entire code be ran from the executable shell script file

    ```$ sh execute.sh```


## Discussion & Results

WSL Problems --- code cannot connect to Postgre since it using a dynamic local host









