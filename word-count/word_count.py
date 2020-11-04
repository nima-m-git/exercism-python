import re

def count_words(sentence):
    counts = {}
    sentence = string_cleaned_list(sentence)

    for numword in sentence:
        count = 0
        for check_match in sentence:
            if numword == check_match:
                count += 1

        counts[numword] = count
    
    return counts


def string_cleaned_list(string):
    string = string.lower() #lowercase
    string = re.sub(r'[.:_,!@$%^&]', ' ', string) # removes all punc but '
    string = re.sub(r'(\W\')|(\'\W)|(^\')|(\'$)', ' ', string) # removes any ' near space
    string = string.strip()
    string = re.split(r'[\s]+', string) #remove all whitespace
    return string

