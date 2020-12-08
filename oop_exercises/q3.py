class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        
        
class Car(Vehicle):
    def __init__(self, name, max_speed, mileage):
        Vehicle.__init__(self, name, max_speed, mileage)
        
        
# From Solution section, it was easier than I thought
class Car(Vehicle):
    pass
        
my_car = Car("self-made", "50", "12421")
print(my_car.name, my_car.max_speed, my_car.mileage)
