class Phone:
  def __init__(self, make, storage, megapixels):
    self.make = make
    self.storage = storage
    self.megapixels = megapixels
    
my_phone = Phone("iPhone", 256, 12)
print(my_phone.make)
print(my_phone.storage)
print(my_phone.megapixels)


#-------------------------------------------
# Private and public

class PrivateClass:
  def __init__(self):
    self.__private_attribute = "I am a private attribute"
    
  def __private_method(self):
    return "I am a private method"
  
  def helper_method(self):
    return self.__private_method()
    
obj = PrivateClass()
print(obj.helper_method())