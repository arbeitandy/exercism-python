def to_rna(dna_strand):
    dna_strand = dna_strand.upper()
    if not set(dna_strand).issubset('ACGT'):
        raise Exception("not a valid dna_strand")
    r = []
    for d in dna_strand:
        if d == 'G':
            r.append('C')
        elif d == 'C':
            r.append('G')
        elif d == 'T':
            r.append('A')
        elif d == 'A':
            r.append('U')

    return "".join(r)


        
