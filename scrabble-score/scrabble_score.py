letter_scores = {
    1: ['a', 'e', 'i', 'o', 'u', 'l', 'n', 'r', 's', 't'],
    2: ['d', 'g'],
    3: ['b', 'c', 'm', 'p'],
    4: ['f', 'h', 'v', 'w', 'y'],
    5: ['k'],
    8: ['j', 'x'],
    10: ['q', 'z']
}
 
letter_scores_spread = {}

for key, values in letter_scores.items():
    for value in values:
        letter_scores_spread[value] = key


def score(word):
    return sum([letter_scores_spread[letter] for letter in word.lower()])


