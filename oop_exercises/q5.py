class Vehicle:
    color = "White"
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass


bus = Bus("school bus", 50, 12)
print(bus.color, bus.name, bus.max_speed, bus.mileage)


car = Car("sample car", 50, 12)
print(bus.color, bus.name, bus.max_speed, bus.mileage)
