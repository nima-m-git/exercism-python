import re


class PhoneNumber:

    def __init__(self, phone_number):
        self.num = phone_number
        self.number = PhoneNumber.number(self)
        self.area_code = self.number[:3]
        if not PhoneNumber.check(self):
            raise ValueError('That is not a valid number')


    def number(self):
        p = re.compile(r'[2-9]{1}\d{,9}')                              
        return ''.join(p.findall(self.num))

            
    def pretty(self):
        sn = self.number
        return f'({sn[:3]}) {sn[3:6]}-{sn[6:10]}' 


    def check(self):
        c = re.compile(r'\d')
        digits = ''.join(c.findall(self.num))
        if digits[0] == '1':
            digits = digits[1:]
        return len(digits)==10 and (int(digits[0]) >1 and int(digits[3]) > 1)


         
        

