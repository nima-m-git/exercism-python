def equilateral(sides):
    if tri_check(sides):
        return len(set(sides)) == 1
    return False


def isosceles(sides):
    if tri_check(sides):
        return len(set(sides)) <= 2
    return False


def scalene(sides):
    if tri_check(sides):
        return len(set(sides)) == 3
    return False


def tri_check(sides):
    for i in sides:
        if i > sum(sides)/2:
            return False
        if i <= 0:
            return False
    return True
    
