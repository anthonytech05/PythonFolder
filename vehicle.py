"""
Create a vehicle parent class with: make, model, year, mileage.
Create a Truck subclass that adds:payload_capacity.
Create a Car subclass that adds: num_doors.
Create 3 vehicle objects(mix of Truck and car).
"""


# Parent Class
class Vehicle:
    def __init__(self, make, model, year, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage


# Truck Subclass
class Truck(Vehicle):
    def __init__(self, make, model, year, mileage, payload_capacity):
        super().__init__(make, model, year, mileage)
        self.payload_capacity = payload_capacity


# Car Subclass
class Car(Vehicle):
    def __init__(self, make, model, year, mileage, num_doors):
        super().__init__(make, model, year, mileage)
        self.num_doors = num_doors


# Create Objects
vehicle1 = Truck("Ford", "F-150", 2020, 45000, 3)
vehicle2 = Car("Toyota", "Camry", 2022, 18000, 4)
vehicle3 = Truck("Mercedes", "Actros", 2019, 120000, 10)


print(vehicle1.make, vehicle1.model, vehicle1.year, vehicle1.mileage, vehicle1.payload_capacity)

print(vehicle2.make, vehicle2.model, vehicle2.year, vehicle2.mileage, vehicle2.num_doors)

print(vehicle3.make, vehicle3.model, vehicle3.year, vehicle3.mileage, vehicle3.payload_capacity)