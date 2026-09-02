from abc import ABC, abstractmethod
# Abstraction means exposing what an object can do while hiding unnecessary implementation details.
# ABC is Abstract Base Class

# DIFFERENCE BETWEEN ABSTRACTION AND ENCAPSULATION
# Encapsulation: How do I control access to the object's data?
# Abstraction: What does the user need to know/use, and what details can remain hidden?

# DIFFERENCE BETWEEN ABSTRACTION AND INHERITANCE
# Inheritance :This class is based on another class.
# Abstraction: Every concrete class of this kind must provide certain behaviour.
# They are often used together, but are not the same

# DIFFERENCE BETWEEN ABSTRACTION AND POLYMORPHISM
# Abstraction defines what must be done. Polymorphism allows different classes to decide how it is done.

# PARENT CLASS
class DeliveryService(ABC):
    def __init__(self, distance):
        self.distance = distance

    # AN ABSTRACT METHOD is not implemented in the parent class
    # but child/sub classes are meant to implement their own version of this method
    @abstractmethod
    def calculate_cost(self):
        # means no implementation is provided here
        pass

    @abstractmethod
    def delivery_time(self):
        pass

    def display_distance(self):
        print(f"Distance is {self.distance} km")
    
# CHILD CLASS
class BikeDelivery(DeliveryService):

    # BikeDelivery's implementation of calculate cost
    def calculate_cost(self):
        return self.distance * 200

    # BikeDelivery's implementation of delivery time
    def delivery_time(self):
        return "2 hours"

class CarDelivery(DeliveryService):
    # CarDelivery's implementation of calculate cost
    def calculate_cost(self):
        return self.distance * 500

    # CarDelivery's implementation of delivery time
    def delivery_time(self):
        return "30 mins"

class ExpressDelivery(DeliveryService):
    # ExpressDelivery's implementation of calculate cost
    def calculate_cost(self):
        return self.distance * 800
        
    # ExpressDelivery's implementation of delivery time
    def delivery_time(self):
        return "20 mins"

# class DroneDelivery(DeliveryService):
#     def calculate_cost(self):
#         return self.distance * 100 
    

bike = BikeDelivery(10)
car = CarDelivery(10)
express = ExpressDelivery(10)

print(bike.calculate_cost())
print(bike.delivery_time())
print(car.calculate_cost())
print(car.delivery_time())
print(express.calculate_cost())
print(express.delivery_time())

# print not needed here because it is alredy printed from the parent class
bike.display_distance()