import random

class Insect:

    def __init__(self,w,l,n):
        self.flight = 0
        self.wings = w
        self.legs = l
        self.name = n
    
    def calc_flight(self): #mutator/set method
        self.flight = random.randint(1,10)
    
    def get_flight(self): #get/accessor method
        return self.flight
    
    def get_name(self): #get/accessor method
        return self.name