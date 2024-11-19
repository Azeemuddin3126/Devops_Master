
class Airplane:
    def __init__(self, first_class, business_class, coach):
        self.passenger_counts = [first_class, business_class, coach]
    
    def total(self):
        return sum(self.passenger_counts)

class Train:
    def __init__(self, car1, car2, car3, car4, car5):
        self.passenger_counts = [car1, car2, car3, car4, car5]
    
    def total(self):
        return sum(self.passenger_counts)

# passengers function
def passengers(obj):
    print(f'There are {obj.total()} passengers on board.')

# Example usage
plane = Airplane(10, 20, 100)
train = Train(30, 25, 40, 35, 20)

passengers(plane)  # Output: There are 130 passengers on board.
passengers(train)  # Output: There are 150 passengers on board.




























class Airplane:
  def __init__(self, first_class, business_class, coach):
    self.first_class = first_class
    self.business_class = business_class
    self.coach = coach
    
  def total(self):
    return self.first_class + self.business_class + self.coach
  
class Train:
  def __init__(self, car1, car2, car3, car4, car5):
    self.car1 = car1
    self.car2 = car2
    self.car3 = car3
    self.car4 = car4
    self.car5 = car5
    
  def total(self):
    return self.car1 + self.car2 + self.car3 + self.car4 + self.car5
  
def passengers(obj):
  print(f'There are {obj.total()} passengers on board.')