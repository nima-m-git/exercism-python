def convert(number):
    sounds = [(3,'Pling'),(5,'Plang'),(7,'Plong')]
    return ''.join([sound for num, sound in sounds if number%num==0]) or str(number)




##    conversion = []
##    string = ''
##
##    def isFactor(factor):
##        return not number%factor
##
##    if isFactor(3):
##        conversion.append('Pling')
##    if isFactor(5):
##        conversion.append('Plang')
##    if isFactor(7):
##        conversion.append('Plong')
##    if not any([isFactor(3), isFactor(5), isFactor(7)]):
##        conversion.append(str(number))
##    return string.join(conversion)
##
