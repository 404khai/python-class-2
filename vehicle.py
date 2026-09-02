# PARENT CLASS
class Vehicle:
    def move(self):
        print("Vehicle is moving")

# CHILD / SUBCLASS
class Car(Vehicle):
    def drive(self):
        print("Car is moving")


car = Car()

car.move()
car.drive()

vehicle = Vehicle()
vehicle.drive()