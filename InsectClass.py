import random

class Insect:

    def __init__(self):
        self.flight = 0
        self.wings = 2
        self.legs = 4
    
    def calc_flight(self):
        self.flight = random.randint(1,10)
    
    def get_flight(self):
        return self.flight