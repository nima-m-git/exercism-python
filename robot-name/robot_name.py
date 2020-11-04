import random, string

class Robot:
    def __init__(self):
        Robot.reset(self)
    

    def new_name():
        '''Generate a new name for factory reset robot,
            in the format: XX###'''
        return ''.join(random.sample(string.ascii_uppercase,2)\
                       +[str(random.randint(0,9)) for _ in range(3)])

     
    def reset(self):
        '''whipe the robots name'''
        random.seed()
        self.name = Robot.new_name()



