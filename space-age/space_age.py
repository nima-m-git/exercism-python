class SpaceAge:
  
    Planet_EY_Ratios = [
        ('earth', 1),
        ('mercury', 0.2408467),
        ('venus', 0.61519726),
        ('mars', 1.8808158),
        ('jupiter', 11.862615),
        ('saturn', 29.447498),
        ('uranus', 84.016846),
        ('neptune', 164.79132)]
        
    def __init__(self, seconds):
        self.sec = seconds
        for planet, ratio in self.Planet_EY_Ratios:
            setattr(self, f'on_{planet}', self.conversion_EY(ratio))
        

    def conversion_EY(self, ratio):
        return lambda r=ratio: round((self.sec/31557600)/ratio, 2)
        #using the lambda here changes the setattr value from float to method
        #
