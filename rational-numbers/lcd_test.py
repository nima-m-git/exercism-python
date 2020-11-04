def lcd(n, d):
    d_a = [i for i in range(1,abs(n)+1) if n%i==0]
    d_b = [i for i in range(1,abs(d)+1) if d%i==0]
    #make a list that only has common values in a and b, find lowest
    lcd = max([denom for denom in d_a if denom in d_b])
    return (n/lcd, d/lcd)

print(lcd(5,10))
