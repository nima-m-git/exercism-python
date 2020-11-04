def is_armstrong_number(number):
    power = len(str(number))
    sep_digits = [digit for digit in str(number)]
    sum_powers = sum([int(digit)**power for digit in sep_digits])
    return sum_powers == number


