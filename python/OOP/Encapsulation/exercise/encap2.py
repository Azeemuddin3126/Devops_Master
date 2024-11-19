class Artist:
    def __init__(self, name, medium, style, famous_artwork):
        self.__name = name
        self.__medium = medium
        self.__style = style
        self.__famous_artwork = famous_artwork

# Initialize an object of the Artist class
my_artist = Artist('Bill Watterson', 'ink and paper', 'cartoons', 'Calvin and Hobbes')

# Trying to access attributes directly will result in an error
try:
    print(my_artist.name)
except AttributeError as e:
    print("Error Message:", e)

try:
    print(my_artist.medium)
except AttributeError as e:
    print("Error Message:", e)

try:
    print(my_artist.style)
except AttributeError as e:
    print("Error Message:", e)

try:
    print(my_artist.famous_artwork)
except AttributeError as e:
    print("Error Message:", e)

# Accessing the attributes using the mangled names
print(my_artist._Artist__name)            # Output: Bill Watterson
print(my_artist._Artist__medium)          # Output: ink and paper
print(my_artist._Artist__style)           # Output: cartoons
print(my_artist._Artist__famous_artwork)  # Output: Calvin and Hobbes
