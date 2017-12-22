"""
A module that contains a function to separate all my groups from the regex group names.

Copyright Gabby Iorg
"""
# step 3: work on Amino acids (p change)
# Separates all my groups into lists
# Get codon

import re
from findercode.variants import SepGroups



def get_groups(df1, df2, df3):
    """ 
    This function separates all the different regex groups. 
    It parses through the subset dataframes and captures variants and then separates the groups (which are the name components).
    
    """
    s = SepGroups()
    print(type(s))

    tst_txt_p1 = " ".join([x for x in df1.iloc[:, 1]])
    P_name = re.compile(
        r"""p\.(?P<wild_typeAA>[GALMFWKQESPVICYHRNDT])(?P<codon>\d+)(?P<variant_AA>\*|[GALMFWKQESPVICYHRNDT]\b)""")


    s["wtaa"] = []
    s["codon_snv"] = []
    s["vnt_AA"] = []
    s["p_change1"] = []

    for n in P_name.finditer(tst_txt_p1):
        s["p_change1"].append(n.group())
        s["wtaa"].append(n.group('wild_typeAA'))
        s["codon_snv"].append(n.group('codon'))
        s["vnt_AA"].append(n.group('variant_AA'))
    # print(len(p_change1))


    tst_txt_p2 = " ".join([x for x in df2.iloc[:, 1]])
    P_name_FS = re.compile(
        r"""(?:p\.)?(?P<wild_typeAA_FS>[GALMFWKQESPVICYHRNDT])(?P<codonFS>\d+)(?P<variant_AA_FS>[GALMFWKQESPVICYHRNDT]|fs)?(?P<stop_pos>fs\*\d+|fs)""")

    s["wtaaFS"] = []
    s["codonFS"] = []
    s["vnt_AAFS"] = []
    s["FSstop_pos"] = []
    s["p_fs2"] = []
    for n in P_name_FS.finditer(tst_txt_p2):
        s["p_fs2"].append(n.group())
        s["wtaaFS"].append(n.group("wild_typeAA_FS"))
        s["codonFS"].append(n.group("codonFS"))
        s["vnt_AAFS"].append(n.group("variant_AA_FS"))
        s["FSstop_pos"].append(n.group("stop_pos"))


    # print(p_fs2)
    # print(FSstop_pos)
    # print(vnt_AAFS)
    
    # This is where I deal with C. names (similar work as in step3)
    # Step 5 work on Bases (c change)
    # Separates all my groups into lists
    # Get WTB, cdna, VntB

    tst_txt_c1 = " ".join([x for x in df1.iloc[:, 2]])
    snv = re.compile(
        r"""c\.(?P<nucltide_pos>\d+)(?P<wild_type_Base>[ACTG])>(?P<variant_Base>[ACTG])""")

    s["Cdna_snv"] = []
    s["WTBsnv"] = []
    s["vnt_Bsnv"] = []

    for n in snv.finditer(tst_txt_c1):
        s["Cdna_snv"].append(n.group('nucltide_pos'))
        s["WTBsnv"].append(n.group('wild_type_Base'))
        s["vnt_Bsnv"].append(n.group('variant_Base'))
    #print(Cdna, WTB, vnt_B)


    tst_txt_c2 = " ".join([x for x in df2.iloc[:, 2]])
    frm_s = re.compile(
        r"""c\.((?P<nucltide_start_FS>\d+)(_|del)(?P<nucltide_end_FS>\d+)?((?P<wildtypeBase>[ACTG]+)|(?P<delins>del|ins))(>)?(?P<variantBaseFS>[ACTG]+)?(?P<insertion>ins[ACTG]+)?)""")

    s["CdnaFS"] = []
    s["raw_WTBFS"] = []
    s["raw_vnt_BFS"] = []
    s["c_fs2"] = []
    for n in frm_s.finditer(tst_txt_c2):
        s["c_fs2"].append(n.group())
        s["CdnaFS"].append(n.group('nucltide_start_FS'))
        s["raw_WTBFS"].append(n.group('wildtypeBase'))
        s["raw_vnt_BFS"].append(n.group('variantBaseFS'))
    #print(CdnaFS, raw_WTBFS, raw_vnt_BFS)


    tst_txt_c3 = " ".join([x for x in df3.iloc[:, 2]])
    splice = re.compile(
        r"""(?:c\.)?(?P<nucltide_pos_spl>\d+)(?P<offset>(\+|-)\d+)(?P<wildtype_Base_spl>[ACTG])>(?P<variantBase_spl>[ACTG])""")

    s["c_splice3"] = [n.group() for n in splice.finditer(tst_txt_c3)]

    s["Cdnaspl"] = []
    s["WTBspl"] = []
    s["vnt_Bspl"] = []
    s["offset_pos"] = []
    for n in splice.finditer(tst_txt_c3):
        s["Cdnaspl"].append(n.group('nucltide_pos_spl'))
        s["offset_pos"].append(n.group('offset'))
        s["WTBspl"].append(n.group('wildtype_Base_spl'))
        s["vnt_Bspl"].append(n.group('variantBase_spl'))
    #print(Cdnaspl, WTBspl, vnt_Bspl, offset_pos)

    # print(c_splice3)
    return s