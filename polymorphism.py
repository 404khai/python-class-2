# Polymorphism means the same method name can behave differently depending on the object using it.
# Simply put Same method, Different objects, Different behaviour
class Car:
    def move(self):
        print("The car is moving")

class Boat:
    def move(self):
        print("The boat is sailing")

class Plane:
    def move(self):
        print("The plane is flying")

car = Car()
boat = Boat()
plane = Plane()

# All three objects use the same method move() but each object performs it differently.
# car.move()
# boat.move()
# plane.move()

# LOOP WITH POLYMORPHISM
# vehicles = [
#     Car(), 
#     Boat(),
#     Plane()
# ]

# vehicle.move() is written only once, But Python decides which version of move() to call based on the actual object.
# for vehicle in vehicles:
#     vehicle.move()

# vehicle = Boat()
# vehicle.move()