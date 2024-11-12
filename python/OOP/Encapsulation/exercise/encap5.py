class Cyclist:
    def __init__(self, name, nationality, nickname):
        self._name = name
        self._nationality = nationality
        self._nickname = nickname

    # Getter and setter for name using property decorator
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # Getter and setter for nationality using property decorator
    @property
    def nationality(self):
        return self._nationality

    @nationality.setter
    def nationality(self, value):
        self._nationality = value

    # Getter and setter for nickname using property decorator
    @property
    def nickname(self):
        return self._nickname

    @nickname.setter
    def nickname(self, value):
        self._nickname = value

# Initialize an object of the Cyclist class
my_cyclist = Cyclist("Greg LeMond", "American", "Le Montstre")

# Accessing attributes using getters
print(my_cyclist.name)          # Output: Greg LeMond
print(my_cyclist.nationality)   # Output: American
print(my_cyclist.nickname)      # Output: Le Montstre

# Modifying attributes using setters
my_cyclist.name = "Eddy Merckx"
my_cyclist.nationality = "Belgian"
my_cyclist.nickname = "The Cannibal"

# Accessing updated attributes
print(my_cyclist.name)          # Output: Eddy Merckx
print(my_cyclist.nationality)   # Output: Belgian
print(my_cyclist.nickname)      # Output: The Cannibal
