class Car:

    def __init__(self,year_model,car_make):
        self.__model = year_model
        self.__make = car_make
        self.__speed = 0

    def set_model(self):
        self.__model = input("Enter the car's year model: ")

    def set_make(self):
        self.__make = input("Enter the car's make: ")

    def set_speed(self):
        current_speed = input("Enter the car's current speed: ")
        self.__speed = int(current_speed)

    def get_model(self):
        return self.__model
    
    def get_make(self):
        return self.__make
    
    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed

        
