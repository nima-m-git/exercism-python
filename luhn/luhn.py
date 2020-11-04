class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(' ', '')


    def double_second(self, num):
        converted = []
        for i, dig in enumerate(reversed(num)):
            if i % 2 != 0:
                if dig >= 5:
                    new = (dig * 2) - 9
                else:
                    new = dig * 2
            else:
                new = dig
            converted.append(new)
        return converted


    def valid(self):
        if (len(self.card_num) >= 2) and (self.card_num.isdigit()):
            return sum(self.double_second([int(x) for x in self.card_num])) % 10 == 0
        return False


