"""
A module that contains 2 functions to create 3 new dataframes for the 3 different kind of variants this program handles. 

Copyright Gabby Iorg

"""
# step 1: get variants I am going to work on

import re
from findercode.variants import GetVariants


def get_variant_data(df):
    """
    This function selects the variants we are going to work on.

    """
    v = GetVariants()
    print(type(v))
    tst_txt_p = " ".join([x for x in df.iloc[:, 1]])
    P_name = re.compile(
        r"""(?:p\.)?(?P<wild_typeAA>[GALMFWKQESPVICYHRNDT])(?P<codon>\d+)(?P<variant_AA>\*|[GALMFWKQESPVICYHRNDT]\b)""")
    P_name_FS = re.compile(
        r"""(?:p\.)?(?P<wild_typeAA_FS>[GALMFWKQESPVICYHRNDT])(?P<codonFS>\d+)(?P<variant_AA_FS>[GALMFWKQESPVICYHRNDT]|fs)?(?P<stop_pos>fs\*\d+|fs)""")

    v["p_change"] = [n.group() for n in P_name.finditer(tst_txt_p)]
    # print(p_change)

    v["p_FS"] = [n.group() for n in P_name_FS.finditer(tst_txt_p)]
    # print(p_FS)

    #listprtn = p_FS + p_change
    # print(listprtn)

    tst_txt_c = " ".join([x for x in df.iloc[:, 2]])
    snv = re.compile(
        r"""(?:c\.)(?P<nucltide_pos>\d+)(?P<wild_type_Base>[ACTG])>(?P<variant_Base>[ACTG])""")
    frm_s = re.compile(
        r"""c\.((?P<nucltide_start_FS>\d+)(_|del)(?P<nucltide_end_FS>\d+)?((?P<wildtypeBase>[ACTG]+)|(?P<delins>del|ins))(>)?(?P<variantBaseFS>[ACTG]+)?(?P<insertion>ins[ACTG]+)?)""")
    splice = re.compile(
        r"""(?:c\.)?(?P<nucltide_pos>\d+)(?P<offset>(\+|-)\d+)(?P<wild_type_Base>[ACTG])>(?P<variant_Base>[ACTG])""")

    v["c_change"] = [n.group() for n in snv.finditer(tst_txt_c)]
    # print(c_change)

    v["c_fs"] = [n.group() for n in frm_s.finditer(tst_txt_c)]
    # print(c_fs)

    #listcdna = (c_fs + c_change)
    # print(listcdna)

    v["c_splice"] = [n.group() for n in splice.finditer(tst_txt_c)]
    # print(c_splice)

    tst_txt_g = " ".join([x for x in df.iloc[:, 0]])
    gene_name = re.compile(
        r"""(?P<Gene_name>CDH1)""")  # Change the gene manually
    v["g_name"] = [n.group() for n in gene_name.finditer(tst_txt_g)]
    # print(g_name)
    return v


def subset_dataframe(df, v):
    """
    This function creates 3 databases from the subset of variants selected.

    """
    df3 = df.loc[df["DNA Sequence Variation"].isin(
        v["c_splice"]) & df["Gene"].isin(v["g_name"])]

    df1 = df.loc[df["Mutation Name"].isin(
        v["p_change"]) & df["DNA Sequence Variation"].isin(v["c_change"]) & df["Gene"].isin(v["g_name"])]

    df2 = df.loc[df["Mutation Name"].isin(
        v["p_FS"]) & df["DNA Sequence Variation"].isin(v["c_fs"]) & df["Gene"].isin(v["g_name"])]

    return df1, df2, df3
    