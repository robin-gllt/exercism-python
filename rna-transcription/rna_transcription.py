def to_rna(dna_strand):

    rna =""    
    for dna in dna_strand:
        if dna == 'G':
            rna+='C'
        elif dna == 'C':
            rna+='G'
        elif dna == 'T':
            rna+='A'
        else:
            rna+='U'
    return rna

#Possible also with translate functions:
# trans = maketrans("GCTA", "CGAU")
# rna = dna.translate(trans)