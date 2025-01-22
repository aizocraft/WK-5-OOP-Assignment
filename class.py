# Assignment 1: Design Your Own Class - Superhero and Villain

# Base class for Superhero
class Superhero:
    def __init__(self, name, power, city, strength_level):
        self.name = name       # Name of the superhero
        self.power = power     # Superpower of the superhero
        self.city = city       # City the superhero protects
        self.__strength_level = strength_level  # Private attribute (Encapsulation)

    def fight_crime(self):
        """Action method for fighting crime"""
        print(f"{self.name} is fighting crime in {self.city} using {self.power}!")

    def fly(self):
        """Action method for flying"""
        print(f"{self.name} is soaring through the sky to protect {self.city}!")

    def train(self, hours):
        """Increase strength level through training"""
        self.__strength_level += hours
        print(f"{self.name} has trained for {hours} hours. New strength level: {self.__strength_level}!")

    def get_strength_level(self):
        """Accessor method to get the strength level"""
        return self.__strength_level


# Inheritance: Villain class inherits from Superhero
class Villain(Superhero):
    def __init__(self, name, power, city, strength_level):
        super().__init__(name, power, city, strength_level)  # Inherit from Superhero constructor

    def fight_crime(self):
        """Override method for Villain's action"""
        print(f"{self.name} is wreaking havoc in {self.city} using {self.power}!")

    def steal(self):
        """Villain's unique action to steal"""
        print(f"{self.name} is stealing in {self.city}!")


# Create instances of Superhero and Villain
hero = Superhero("Captain Code", "Super Strength", "Tech City", 90)
villain = Villain("Dark Coder", "Dark Web Manipulation", "Tech City", 70)

# Call methods for Hero and Villain
hero.fight_crime()  # Fighting crime with hero
hero.fly()          # Hero flying through the sky
hero.train(10)      # Hero training to get stronger
villain.fight_crime()  # Villain causing destruction
villain.steal()        # Villain stealing
print(f"{hero.name}'s strength level: {hero.get_strength_level()}")
