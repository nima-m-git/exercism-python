def value(colors):
    return int(''.join([str(color_codes[color]) \
                        for color in colors if color in color_codes][:2]))
   

  
color_codes = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green' : 5,
    'blue' : 6,
    'violet' : 7,
    'grey' : 8,
    'white' : 9,
    }



