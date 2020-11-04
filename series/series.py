def slices(series, length):
    sl = len(series)
    l = length

    if not (sl and l > 0): 
        raise ValueError('The series length and length must be positive values')
    if not isinstance(l, int):
        raise TypeError('The length must be an integer')
    if not sl >= l:
        raise ValueError('The length cannot be longer than the series')

    #return [series[a:b] for a,b in zip(range(0,(sl-l+1)), range((l),sl+1))]
    return [series[i:(i+l)] for i in range(0,sl-l+1)]

#   Breaking down the problem:
##    eg [123456] [3]
##    series length = sl
##    length = l
##    first slice: (series)[0:(l+1)]
##    next slice:  (series)[1:(l+2)]
##    last slice:  (series)[(sl-l):(sl)]
##
##    make list of numbers, 


