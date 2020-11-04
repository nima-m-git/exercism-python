import re

def is_valid(isbn_raw): 
    isbn_clean = list(isbn_raw.replace('-',''))
    
    if not is_valid_format(isbn_clean):
        return False
    
    isbn_num = isbn_to_num(isbn_clean)
    
    return (isbn_math(isbn_num))
        

def is_valid_format(isbn_clean):
    ''' check if isbn string is in valid format'''
    if len(isbn_clean) == 10:
        return re.match('[0-9]{9}[0-9|X]', isbn_clean)
            

def isbn_to_num(isbn_clean):
    if isbn_clean[-1] == 'X':
        isbn_clean[-1] = '10'
    return [int(isbn_clean[i]) for i in range(10)]

    
def isbn_math(isbn_num):
    paired = list(zip(isbn_num, ([i for i in range(1,11)][::-1])))
    sum_paired = sum([a * b for a, b in paired])
    return sum_paired % 11 == 0
 

