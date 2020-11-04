day_verse = ['zeroth','first','second','third','fourth','fifth','sixth','seventh','eighth','ninth','tenth','eleventh','twelfth']

gifts = [
        'and a Partridge in a Pear Tree.',
        'two Turtle Doves, ',
        'three French Hens, ',
        'four Calling Birds, ',
        'five Gold Rings, ',
        'six Geese-a-Laying, ',
        'seven Swans-a-Swimming, ',
        'eight Maids-a-Milking, ',
        'nine Ladies Dancing, ',
        'ten Lords-a-Leaping, ',
        'eleven Pipers Piping, ',
        'twelve Drummers Drumming, ',
]

one_gift = 'a Partridge in a Pear Tree.'


def recite(start_verse, end_verse):
    return [song(verse) for verse in range(start_verse, end_verse+1)]

def song(verse):
    first_verse = f'On the {day_verse[verse]} day of Christmas my true love gave to me: '

    if verse == 1:
        song = first_verse + one_gift
    else:    
        gifts_given = ''.join([gift for gift in gifts[0:verse]][::-1])
        song = first_verse + gifts_given
        
    return song



