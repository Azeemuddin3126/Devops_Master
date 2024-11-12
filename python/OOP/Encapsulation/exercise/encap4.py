class Dancer:
  def __init__(self, name, nationality, style):
    self._name = name
    self._nationality = nationality
    self._style = style
    
  def get_name(self):
    return self._name
  
  def set_name(self, new_value):
    self._name = new_value
    
  def get_nationality(self):
    return self._nationality
  
  def set_nationality(self, new_value):
    self._nationality = new_value
    
  def get_style(self):
    return self._style
  
  def set_style(self, new_value):
    self._style = new_value
    
  name = property(get_name, set_name)
  nationality = property(get_nationality, set_nationality)
  style = property(get_style, set_style)

# Initialize an object of the Dancer class
my_dancer = Dancer("Savion Glover", "American", "tap")

# Accessing attributes using getters
print(my_dancer.name)           # Output: Savion Glover
print(my_dancer.nationality)    # Output: American
print(my_dancer.style)          # Output: tap

# Modifying attributes using setters
my_dancer.name = 'Anna Pavlova'
my_dancer.nationality = 'Russian'
my_dancer.style = 'ballet'

# Accessing updated attributes
print(my_dancer.name)           # Output: Anna Pavlova
print(my_dancer.nationality)    # Output: Russian
print(my_dancer.style)          # Output: ballet
