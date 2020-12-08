class Vehicle():
    def __init__(self, max_speed, milleage):
        self.max_speed = max_speed
        self.milleage = milleage
        
car = Vehicle(25, 2)
print(car.max_speed)
print(car.milleage)
