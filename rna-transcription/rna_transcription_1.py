def to_rna(dna_strand):
    return ''.join([rna for nuc in dna_strand for dna, rna in dna_rna  \
                    if dna == nuc])


dna_rna = [
    ('G','C'),
    ('C','G'),
    ('T','A'),
    ('A','U'),
    ]

