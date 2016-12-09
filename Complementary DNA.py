# Complementary DNA

# my original code
def DNA_strand(dna):
    strand = ""
    for i in dna:
        if i == 'A':
            strand += 'T'
        elif i == 'T':
            strand += 'A'
        elif i == 'C':
            strand += 'G'
        else:
            strand += 'C'
    return strand

# Better code shown
import string
def DNA_strand(dna):
    return dna.translate(string.maketrans('ATTGC', 'TAACG'))
