def convert(number):
    conversion = []
    string = ''

    def isFactor(factor):
        return not number%factor

    if isFactor(3):
        conversion.append('Pling')
    if isFactor(5):
        conversion.append('Plang')
    if isFactor(7):
        conversion.append('Plong')
    if not any([isFactor(3), isFactor(5), isFactor(7)]):
        conversion.append(str(number))
    return string.join(conversion)
