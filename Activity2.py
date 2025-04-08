# Activity 2: Polymorphism Challenge (Animals or Vehicles)

# Vehicle Class
class Vehicle:
    def move(self):
        print("Moving forward...")

# Car Class inherits from Vehicle
class Car(Vehicle):
    def move(self):
        # Polymorphism: Car defines its own move method
        print("Driving on the road")

# Plane Class inherits from Vehicle
class Plane(Vehicle):
    def move(self):
        # Polymorphism: Plane defines its own move method
        print("Flying in the sky")

# Dog Class (Non-Vehicle, but uses the same method for polymorphism)
class Dog:
    def move(self):
        # Polymorphism: Dog defines its own move method
        print("Running on the ground")

# Create instances
vehicle = Vehicle()
car = Car()
plane = Plane()
dog = Dog()

# Demonstrating Polymorphism
vehicles = [vehicle, car, plane, dog]

for v in vehicles:
    v.move()  # Calls the appropriate move() method for each object


