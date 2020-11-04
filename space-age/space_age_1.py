class SpaceAge:
  
    
    def __init__(s, seconds):
        s.sec = seconds
        s.e_y = s.sec/31557600

    def on_earth(s):
        return round2(s.e_y/1)

    def on_mercury(s):
        return round2(s.e_y/.2408467) 

    def on_venus(s):
        return round2(s.e_y/0.61519726)

    def on_mars(s):
        return round2(s.e_y/1.8808158)

    def on_jupiter(s):
        return round2(s.e_y/11.862615)

    def on_saturn(s):
        return round2(s.e_y/29.447498)

    def on_uranus(s):
        return round2(s.e_y/84.016846)

    def on_neptune(s):
        return round2(s.e_y/164.79132)
        

def round2(num):
    return round(num, 2)

