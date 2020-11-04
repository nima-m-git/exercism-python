def leap_year(year):
    #leap if: true, and (not true or true)
    div4 = year%4==0
    div100 = year%100==0 #if this, div4 at least true
    div400 = year%400==0 #if this, rest are true
    if div400:
        return True
    elif div100: 
        return False
    elif div4:
        return True
    else:
        return False

    
