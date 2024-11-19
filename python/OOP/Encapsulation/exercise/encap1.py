class Country:
    def __init__(self, name, capital, population, continent):
        self._name = name
        self._capital = capital
        self._population = population
        self._continent = continent

# Initialize an object of the Country class
my_country = Country('France', 'Paris', 67081000, 'Europe')

# Accessing the private attributes (not recommended, but for the exercise purpose)
print(my_country._name)       # Output: France
print(my_country._capital)    # Output: Paris
print(my_country._population) # Output: 67081000
print(my_country._continent)  # Output: Europe