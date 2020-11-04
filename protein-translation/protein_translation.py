def proteins(strand):
    def convert_to_codon(strand):
        #break strand into blocks of 3
        #splice in intervals of 3? and add to list (eg 0:3, 3:6, 6:9, for len 9)
        return [strand[i:i+3] for i in range(0, len(strand), 3)]
 
    #match value/codon to key/protein, stopping if STOP codon
    proteins = []
    codons = convert_to_codon(strand)
    for codon in codons:
        protein = ''.join([k for k,v in protein_codon_dic.items() if codon in v])
        if protein == 'STOP':
            break
        proteins.append(protein)

    return proteins
        




protein_codon_dic = {
    'Methionine': ['AUG'],
    'Phenylalanine': ['UUU', 'UUC'],
    'Leucine': ['UUA', 'UUG'],
    'Serine': ['UCU','UCC','UCA','UCG'],
    'Tyrosine': ['UAU', 'UAC'],
    'Cysteine': ['UGU','UGC'],
    'Tryptophan': ['UGG'],
    'STOP': ['UAA','UAG','UGA'],
    }

