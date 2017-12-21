"""

A module that contains a translator for Amino Acids' single letter code to three letter code

Copyright Gabby Iorg

"""

def AA_translator (oneAA=[]):
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

