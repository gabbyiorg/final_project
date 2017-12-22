"""
A module with a function to obtain the name of the excel table from the scientific paper;
this is where the data to be manipulated is found. 

It also contains a function to read-in the initial excel table.
The table is manipulated and converted into a pandas dataframe.

Copyright Gabby Iorg
"""

import os
import pandas as pd


def get_filename():
    """It gets user input for the table name"""
    
    table_name = input(
        "Please enter the name of the excel table of your interest in the format, Name.xlsx:  ")
    if not os.path.exists(table_name):
        print("%s does not exist" % table_name)
        return get_filename()
    else:
        return table_name


def read_ini_table(table_name=""):
    """This function asks for the excel table that we are going to extract the variants from.

        For DEMO please use: example.xlsx """

    df = pd.read_excel(table_name, header=1)
    columns = ['Gene', 'Mutation Name',
               'DNA Sequence Variation', 'Tumor Site', 'Gender', 'Race']
    df[columns] = df[columns].fillna("")
    df.sort_values('DNA Sequence Variation', ascending=True, inplace=True)
    df.drop_duplicates(['DNA Sequence Variation'], inplace=True)
    return df