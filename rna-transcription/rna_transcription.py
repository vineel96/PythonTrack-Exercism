def to_rna(dna_strand):
    trans=str.maketrans('GCTA','CGAU')
    return dna_strand.translate(trans)
