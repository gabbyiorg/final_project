# Variant Finder

This program will read in an excel table with variant names found in (mostly) supplemental material from scientific papers.
It will scan the table to find c. or p. names of variants.
It will then grab those rows in which variant names are found and manipulate them to present a final pandas dataframe with: the full name in HGVS nomenclature standards, the gene in which the variant has been reported, the base change position, the codon position, the Wildtype Seq(or base), the variant seq(base), Wildtype AA, and Variant AA.

There are two classe to put a spot light or keep track of the number of variants you are currently working on.  
And there is a graph which will separate the variants by gene and give you a visual representation of the amount of variants found per gene in a given paper. 

## Background information: 

HGVS general recommendations*: 
 - All variants should be described at the most basic level, the DNA level. Descriptions at the RNA and/or protein level may be given in addition.
 - All variants should be described in relation to an accepted reference sequence. 
 - A letter prefix should be used to indicate the type of reference sequence used. This program will only use c. and p. prefixes:
 
  -“c.” for a coding DNA reference sequence
  
  -“p.” for a protein reference sequence
  
   Other prefixes not used in Variant Finder are:
       - “g.” for a genomic reference sequence
       - “n.” for a non-coding DNA reference sequence
       - “r.” for an RNA reference sequence (transcript).
       
- Descriptions at DNA and protein level are clearly different:

-DNA-level 123456A>T: number(s) referring to the nucleotide(s) affected, nucleotides in CAPITALS using IUPAC-IUBMB assigned nucleotide symbols.
       
-Protein level Lys76Asn: the amino acid(s) affected in 3- or 1-letter followed by a number IUPAC-IUBMB assigned amino acid symbols 
    
**three-letter amino acid code is preferred (see Standards)

*More detail information about variant nomenclature can be found at [here](http://varnomen.hgvs.org/recommendations/general/)

Definitions: 

Base: Also known as Nucleobases, or nitrogenous bases or often simply bases, are nitrogen-containing biological compounds that form nucleosides, and constitute the basic building blocks of nucleic acids. Five nucleobases—adenine (A), cytosine (C), guanine (G), thymine (T), and uracil (U)—are called primary or canonical. They function as the fundamental units of the genetic code, with the bases A, G, C, and T being found in DNA while A, G, C, and U are found in RNA. Thymine and uracil are identical excepting that T includes a methyl group that U lacks.
```
       A<->T or U
       G<->C
```
AA = amino acids
 Amino acids are the building blocks from which proteins are constructed. These organic compounds are coded by a triplet of DNA bases. There are 20 of them that are coded by a genetic sequences.
          
   Arginine        R
   Asparagine      N
   Aspartic acid   D
   Cysteine        C
   Glutamic acid   E
   Glutamine       Q
   Glycine         G
   Histidine       H 
   Isoleucine      I
   Leucine         L 
   Lysine          K
   Methionine      M
   Phenylalanine   F
   Proline         P
   Serine          S
   Threonine       T
   Tryptophan      W
   Tyrosine        Y
   Valine          V

Codon: A unit that consists of three adjacent bases on a DNA molecule and that determines the position of a specific amino acid in a protein molecule during protein synthesis.

Wildtype: The form or forms of a gene sequence commonly occurring in nature in a given species. 

Variant: An alteration in the most common DNA base(s) sequence. 
