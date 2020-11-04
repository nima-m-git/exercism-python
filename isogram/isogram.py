import re

def is_isogram(string):
    c_string = re.sub(r'[ -]', '', string).lower()
    if len(set(c_string)) == len(c_string):
        return True
    return False
    
    
