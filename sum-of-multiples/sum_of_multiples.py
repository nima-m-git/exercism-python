def sum_of_multiples(limit, multiples):
    return sum({
        x
        for multiple in multiples
        for x in range(multiple, limit, multiple)
    })
