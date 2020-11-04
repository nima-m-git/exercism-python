def distance(strand_a, strand_b):
    '''return the number of characters that do not match'''
    if len(strand_a) != len(strand_b):
        raise ValueError('Strands must be the same length!')
    return sum([a != b for a, b in zip(strand_a, strand_b)])

        
