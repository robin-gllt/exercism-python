import random

class Robot(object):

    robot_history = []

    def __init__(self): 
        while True:
            self.name = chr(random.randint(65,90))
            self.name += chr(random.randint(65,90))
            self.name += str(random.randint(100,999))
            if self.name not in self.robot_history:
                break 

        self.robot_history.append(self.name)

    #reset the Robot
    def reset (self):
        self.robot_history.remove(self.name)
        self.__init__()
 
