import numpy

def largest(min_factor, max_factor):
    value_check(min_factor, max_factor)
    
    products, factors = get_factors(min_factor, max_factor)
    if not factors:
        return None, []

    largest = max(products)
    largest_factors = [factor for factor in factors if product(factor) == largest]
        
    return (largest, largest_factors)


def smallest(min_factor, max_factor):
    value_check(min_factor, max_factor)
    
    products, factors = get_factors(min_factor, max_factor)
    if not factors:
        return None, []
    smallest = min(products)
    smallest_factors = [factor for factor in factors if product(factor) == smallest]
    
    return (smallest, smallest_factors)
    
    
    
def is_palindrome(number):
    return list(str(number)) == list(str(number))[::-1]


def get_factors(low, high):
    factors = [[a,b] for a in range(low, high+1) for b in range(low, high+1) if a >= b and is_palindrome(a*b)]
    products = [product(factor) for factor in factors]
    return products, factors


def product(factor):
    return numpy.prod(factor)


def value_check(min_factor, max_factor):
    if max_factor < min_factor or min_factor < 0:
        raise ValueError('Those are invalid values')

print(smallest(10,99))



    
