"""
A module to hold all my classes

"""


class GetVariants(dict):

    """
    A class to obtain the p. and the c. regex group names

    """
    def __init__(self, variant_types=None):
        if variant_types == None:
            super(GetVariants, self).__init__([("g_name", []),
                                               ("c_change", []),
                                               ("p_change", []),
                                               ("p_change", []),
                                               ("c_splice", []),
                                               ("p_FS", []),
                                               ("c_fs", [])])

    def __str__(self):
        keys = list(self.keys())
        keys.sort()
        tmp = "Variant types:\n"
        for key in keys:
            tmp = tmp + "%s: %s\n" % (key, len(self[key]))
        return tmp


class SepGroups (dict):
    """
    A class to separate all my groups from the regex group names and store them in a dictionary.  

    """
    def __init__(self, variant_types2=None):
        if variant_types2 == None:
            super(SepGroups, self).__init__([("wtaa", []),
                                             ("codon_snv", []),
                                             ("vnt_AA", []),
                                             ("p_change1", []),
                                             ("wtaaFS", []),
                                             ("codonFS", []),
                                             ("vnt_AAFS", []),
                                             ("FSstop_pos", []),
                                             ("p_fs2", []),
                                             ("Cdna_snv", []),
                                             ("WTBsnv", []),
                                             ("vnt_Bsnv", []),
                                             ("CdnaFS", []),
                                             ("raw_WTBFS", []),
                                             ("raw_vnt_BFS", []),
                                             ("c_fs2", []),
                                             ("c_splice3", []),
                                             ("Cdnaspl", []),
                                             ("WTBspl", []),
                                             ("vnt_Bspl", []),
                                             ("offset_pos", [])])

    def __str__(self):
        keys = list(self.keys())
        keys.sort()
        tmp = "No. of variants found per Group (name components):\n"
        for key in keys:
            tmp = tmp + "%s: %s\n" % (key, len(self[key]))
        return tmp


class ConstFullName(dict):

    """
    A class to construct variants full names

    """
    def __init__(self, variant_types3=None):
        if variant_types3 == None:
            super(ConstFullName, self).__init__([("pfullname", []),
                                                 ("snv_vnt_fullname", []),
                                                 ("pfullnameFS", []),
                                                 ("vnt_fullnameFS", [])])

    def __str__(self):
        keys = list(self.keys())
        keys.sort()
        tmp = "Variant names' types:\n"
        for key in keys:
            tmp = tmp + "%s: %s\n" % (key, len(self[key]))
        return tmp
    
    
class Variant(object):
    """
    A class to get the variants'names and the gene we are interested on. 
    This class also keeps a tali of the variants on spot light.
    """
    num_variants = 0

    def __init__(self, vname="", gene=""):
        self.vname = vname
        self.gene = gene

        Variant.num_variants += 1

    @property
    def vname(self):
        return self.__vname

    @vname.setter
    def vname(self, vname):
        self.__vname = str(vname).strip()

    @property
    def gene(self):
        return self.__gene

    @gene.setter
    def gene(self, gene):
        if not isinstance(gene, str):
            raise AttributeError("Gene name must be a string")
        self.__gene = gene

    @classmethod
    def how_many(cls):
        """Prints the current number of variants."""
        print("There are {} variants to work with.".format(cls.num_variants))

    def del_variant(self):
        print("You are deleting the variant {}".format(self.vname))
        Variant.num_variants -= 1

        if Variant.num_variants == 0:
            print("There are no more variants to work with.")
        else:
            print(
                "There are/is {} more variant(s) to work with.".format(Variant.num_variants))

    def __str__(self):
        return "The variant {}, is located in the {} gene".format(self.vname, self.gene)    

    
    
class VntCount(Variant):
    """
    A class that inherits from the Variant class.
    Returns the number of variants from the dataframe and the number of active instances
    """

    def __init__(self, dataF, dfname="Interesting table", *args, **kwargs):

        super(VntCount, self).__init__(*args, **kwargs)
        self.dataF = dataF
        self.dfname = dfname

        def num_variants(self):
            num = dataF.shape[0]
            return num
        self.num = num_variants(self)

    @property
    def dfname(self):
        return self.__dfname

    @dfname.setter
    def dfname(self, dfname):
        self.__dfname = str(dfname).strip()

    def __str__(self):
        return "There are {} {} variants in the {} dataframe.\nBut you are only working with {} variants from this table.".format(self.num,                                                                                                                                  self.gene,                                                                                                                                self.dfname,                                                                                                                       Variant.num_variants)
    
    
   