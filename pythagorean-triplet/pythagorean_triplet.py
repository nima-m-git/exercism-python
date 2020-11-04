def triplets_with_sum(number):
    opts = list(range(number))
    trips = [[a,b,c] for a in opts for b in opts for c in opts \
             if (a+b+c) == number and (a<b<c) and (a**2 + b**2 == c**2)]
    return trips







def triplets_in_range(start, end):
    pass


def is_triplet(triplet):
    pass
