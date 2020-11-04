def primes(limit):
    all = list(range(2, limit+1))

    for i in all:
        for x in range(2, round(limit/i)+1): 
            if (i*x) in all:
                all.remove(i*x)
    return all
    
