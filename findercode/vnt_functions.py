"""

A module that contains three different functions: 
    - a translator for Amino Acids' single letter code to three letter code.
    - a little text "cleaner"
    - a graph generator

Copyright Gabby Iorg

"""

import matplotlib.pyplot as plt; plt.rcdefaults()

def AA_translator(oneAA=[]):
    """
    oneAA: a list containing one letter amino acid codes (strings)
    Variants can also contain "*" which mean they code for a "stop" sequence
    None deals with frame shift nomenclature
    
    returns: a list containing Three letter amino acid codes (strings)"""
   
    AADICT = {"A":"Ala ", "None":"None ",
              "C":"Cys ", 
              "D":"Asp ",
              "E":"Glu ",
              "F":"Phe ",
              "G":"Gly ",
              "H":"His ",
              "I":"Ile ",
              "K":"Lys ",
              "L":"Leu ",
              "M":"Met ",
              "N":"Asn ",
              "P":"Pro ",
              "Q":"Gln ",
              "R":"Arg ",
              "S":"Ser ",
              "T":"Thr ",
              "V":"Val ",
              "W":"Trp ",
              "Y":"Tyr ",
              "*":"* "}

    Three_letter = "".join(str(AADICT.get(letter, letter)) for letter in oneAA)
    #Translation = [Three_letter[i:i+3] if i != "*" else Three_letter.split("*") for i in range (0, len(Three_letter), 3)]
    Translation = Three_letter.split()
    return Translation


def sub_nones_empty(vntlist):
    """This function substitutes the value None for an empty string"""
    empstr = ['' if v is None else v for v in vntlist]
    return empstr



def graphing(data_fr):
    """
    This function graphs our final dataframe. It will return a bar graph which will separate the variants by gene and give you a visual representation of the amount of variants found per gene in a given paper.
    
    It takes a pandas dataframe as an argument and returns a bar graph
    """
    graphdb1 = data_fr.drop(["Wildtype_Amino_Acid", "Codon", "Variant_Amino_Acid", "Wildtype_Seq", "Cdna_Position_Number",
                             "Variant_Seq"], axis=1, inplace=False)
    graphdb = graphdb1.groupby("Gene_Name").count()
    graphdb.columns = ['Variant_Count']
    graphdb.plot(kind='barh', title="No. of Variants found by Gene", color='pink')
    plt.show()
    answ = input(
            "Would you like to save the graph?: yes or no ")
    if answ == "yes":
        plt.savefig('Variants_by_gene.png', bbox_inches='tight')
        print("\n Ok it is saved!") 
        print("  Thank you for using Variant Finder. Bye!")
    else:
        print("ok, thank you for using Variant Finder. Bye!")
    return 