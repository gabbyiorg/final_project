"""

A module that contains a function to read in the initial excel table.
The table is manipulated and converted into a pandas dataframe.

Copyright Gabby Iorg

"""

def read_ini_table():
    """This function asks for the excel table that we are going to extract the variants from.

        For DEMO please use: example.xlsx """

    table_name = input(
        "Please enter the name of the excel table of your interest in the format, Name.xlsx:  ")
    try:
        df = pd.read_excel(table_name, header=1)
        columns = ['Gene', 'Mutation Name',
                   'DNA Sequence Variation', 'Tumor Site', 'Gender', 'Race']
        df[columns] = df[columns].fillna("")
        df.sort_values('DNA Sequence Variation', ascending=True, inplace=True)
        df.drop_duplicates(['DNA Sequence Variation'], inplace=True)
        return df
    except NameError:
         print("Invalid .xlsx file")