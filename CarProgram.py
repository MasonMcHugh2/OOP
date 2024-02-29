import CarClass as c

def main():

    year_model = 0
    car_make = ' '

    Car = c.Car(year_model, car_make)

    Car.set_model()
    Car.set_make()
    Car.set_speed()
    
    Car.get_model()
    Car.get_make()
    Car.get_speed()
    
    
    for i in range(5):
        Car.accelerate()
        print(f"Accelerate to {Car.get_speed()}")

    for i in range(5):
        Car.brake()
        print(f"Brake to {Car.get_speed()}")
    
main()