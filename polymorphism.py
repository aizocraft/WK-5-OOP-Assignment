# Improved Polymorphism Challenge - Vehicles and Animals

# Base class for Vehicles
class Vehicle:
    def __init__(self, speed, fuel):
        self.speed = speed  # Speed of the vehicle (in km/h)
        self.fuel = fuel    # Fuel level (percentage)

    def move(self):
        """Generic move method that will be overridden by subclasses."""
        raise NotImplementedError("This method should be overridden by subclasses.")

    def refuel(self):
        """Method to refuel the vehicle."""
        self.fuel = 100
        print(f"Vehicle is refueled! Current fuel level: {self.fuel}%")

    def check_status(self):
        """Display the vehicle's status."""
        print(f"Speed: {self.speed} km/h, Fuel: {self.fuel}%")

# Car class inherits from Vehicle
class Car(Vehicle):
    def move(self):
        if self.fuel > 0:
            print(f"The car is driving at {self.speed} km/h 🚗")
        else:
            print("Out of fuel! Refuel the car.")

# Plane class inherits from Vehicle
class Plane(Vehicle):
    def move(self):
        if self.fuel > 0:
            print(f"The plane is flying at {self.speed} km/h ✈️")
        else:
            print("Out of fuel! Refuel the plane.")

# Boat class inherits from Vehicle
class Boat(Vehicle):
    def move(self):
        if self.fuel > 0:
            print(f"The boat is sailing at {self.speed} km/h 🚢")
        else:
            print("Out of fuel! Refuel the boat.")

# Base class for Animals
class Animal:
    def move(self):
        """Generic move method that will be overridden by subclasses."""
        raise NotImplementedError("This method should be overridden by subclasses.")

# Dog class inherits from Animal
class Dog(Animal):
    def move(self):
        print("The dog is running 🐕")

# Fish class inherits from Animal
class Fish(Animal):
    def move(self):
        print("The fish is swimming 🐟")

# Bird class inherits from Animal
class Bird(Animal):
    def move(self):
        print("The bird is flying 🦅")

# Create instances of Vehicle and Animal
vehicles = [
    Car(speed=120, fuel=50),
    Plane(speed=800, fuel=75),
    Boat(speed=30, fuel=40)
]

animals = [
    Dog(),
    Fish(),
    Bird()
]

# Demonstrate polymorphism for Vehicles: Calling move() for each vehicle
print("Vehicles in action:")
for vehicle in vehicles:
    vehicle.check_status()  # Show vehicle status
    vehicle.move()          # Call move method specific to each vehicle

# Refuel all vehicles
print("\nRefueling vehicles:")
for vehicle in vehicles:
    vehicle.refuel()

# Demonstrate polymorphism for Animals: Calling move() for each animal
print("\nAnimals in action:")
for animal in animals:
    animal.move()  # Each animal moves differently

