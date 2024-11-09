"""
Class: A blueprint for creating objects. It defines the attributes and methods that the object will have.

Object: An instance of a class. Each object can have its own data, but it follows the structure defined by its class.

Instance: A specific object created from a class.

Instantiate: The process of creating an object from a class.

"""

# Define a class called Dog
class Dog:
    # Class attribute shared by all instances
    species = "Canis lupus"

    # Constructor method to initialize attributes
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

    # Instance method to describe the dog
    def describe(self):
        return f"{self.name} is {self.age} years old."

    # Instance method to check if the dog is a puppy
    def is_puppy(self):
        return self.age < 1

# Instantiate (create) objects from the Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 0.5)

# Accessing instance attributes
print(dog1.name)       # Output: Buddy
print(dog1.age)        # Output: 3

# Calling instance methods
print(dog1.describe())   # Output: Buddy is 3 years old.
print(dog2.describe())   # Output: Max is 0.5 years old.
print(dog2.is_puppy())   # Output: True

# Accessing class attribute
print(dog1.species)    # Output: Canis lupus
print(dog2.species)    # Output: Canis lupus

#----------------------------------------------

class Actor:
    """Define the actor class"""
    def __init__(self, first_name, last_name, birthday, total_films, oscar_nominations=0, oscar_wins=0):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.total_films = total_films
        self.oscar_nominations = oscar_nominations
        self.oscar_wins = oscar_wins
    
helen = Actor("Helen", "Mirren", "July 26", 80, 4, 1)
dwayne = Actor("Dwayne", "Johnson", "July 9", 34)

print(f'{helen.first_name} won {helen.oscar_wins} oscar(s).')
print(f'{dwayne.first_name} won {dwayne.oscar_wins} oscar(s).')

#---------------------------------------------------

import copy

# Create a nested list object
original_list = [1, [2, 3], 4]

# Shallow copy
shallow_copied_list = copy.copy(original_list)
# Deep copy
deep_copied_list = copy.deepcopy(original_list)

# Modify the nested list in the original
original_list[1][0] = 'X'

# Results
print(shallow_copied_list)  # Output: [1, ['X', 3], 4]
print(deep_copied_list)     # Output: [1, [2, 3], 4]

#---------------------------------------------------------
#labs

class SuperHero:
    def __init__(self, name, secret_identity, powers):
        self.name = name
        self.secret_identity = secret_identity
        self.powers = powers

# Test the code
hero = SuperHero(
    "Spider-Man", 
    "Peter Parker", 
    [
        "superhuman strength", 
        "superhuman speed", 
        "superhuman reflexes", 
        "superhuman durability", 
        "healing factor", 
        "spider-sense alert", 
        "heightened senses", 
        "wallcrawling"
    ]
)

print(hero.name)            # Output: Spider-Man
print(hero.secret_identity) # Output: Peter Parker
print(hero.powers)          # Output: List of powers
#--------------------------------------------------

class Observation:
    def __init__(self, date, temperature, elevation, penguins, precipitation=0):
        self.date = date
        self.temperature = temperature
        self.elevation = elevation
        self.penguins = penguins
        self.precipitation = precipitation

# Test the code
observation = Observation(
    "October 26, 2019", 
    -47.0, 
    329.4, 
    3
)

print(observation.date)           # Output: October 26, 2019
print(observation.temperature)    # Output: -47.0
print(observation.elevation)      # Output: 329.4
print(observation.penguins)       # Output: 3
print(observation.precipitation)  # Output: 0 (default value)

#------------------------------------------

class BigCat:
    genus = "panthera"  # Class attribute shared by all instances
    
    def __init__(self, species, common_name, habitat):
        self.species = species
        self.common_name = common_name
        self.habitat = habitat

# Test the code
big_cat = BigCat("tigris", "tiger", ["asia"])

print(big_cat.genus)        # Output: panthera
print(big_cat.species)      # Output: tigris
print(big_cat.common_name)  # Output: tiger
print(big_cat.habitat)      # Output: ['asia']

