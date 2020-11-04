def classify(n):

    if not n > 0:
        raise ValueError('number must be a positive integer')
  
    aliquot = sum([i for i in range(1,n) if n%i==0])

    if aliquot == n:
        return 'perfect'
    if aliquot > n:
        return 'abundant'
    if aliquot < n:
        return 'deficient'
