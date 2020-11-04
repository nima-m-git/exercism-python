def tri_check(triangle):
    def wrapper(sides):
        def conditions(sides):
            for i in sides:
                if i > sum(sides)/2:
                    return False
                if i <= 0:
                    return False
            return True
        return conditions(sides) and triangle(sides)
    return wrapper


@tri_check
def equilateral(sides):
    return len(set(sides)) == 1



@tri_check
def isosceles(sides):
    return len(set(sides)) <= 2



@tri_check
def scalene(sides):
    return len(set(sides)) == 3

    


