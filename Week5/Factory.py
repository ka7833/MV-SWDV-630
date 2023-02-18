class Car:
    def __init__(self, name):
        self.name = name

class CarFactory:
    def create_car(self, car_type):
        if car_type == "sedan":
            return Car("Sedan Car")
        elif car_type == "suv":
            return Car("SUV Car")
        elif car_type == "hatchback":
            return Car("Hatchback Car")

factory = CarFactory()
sedan = factory.create_car("sedan")
suv = factory.create_car("suv")
hatchback = factory.create_car("hatchback")

print(sedan.name) # Output: Sedan Car
print(suv.name) # Output: SUV Car
print(hatchback.name) # Output: Hatchback Car
