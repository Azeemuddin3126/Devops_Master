class Alpha:
  def show(self):
    print("I am from class Alpha")
  
  def hello(self):
    print("Hello from Alpha")
    
class Bravo(Alpha):
  def show(self):
    print("I am from class Bravo")
  
  def hello(self):
    print("Hello from Bravo")
    
test_object = Alpha()
test_object.hello()

#---------method overloading

class TestClass:
  def sum(self, a = 0, b = 0, c = 0):
    if a != 0 and b != 0 and c != 0:
      return a + b + c
    elif a != 0 and b != 0:
      return a + b
    elif a != 0:
      return a
    else:
      return 0
    
obj = TestClass()
print(obj.sum(0, 2))

#----------------operator overloading

class FinancialAccount:
  def __init__(self, amount):
    self.account = amount
    
  def __add__(self, other):
    return self.account + other.account
    
class BankAccount(FinancialAccount):
  pass

class InvestmentAccount(FinancialAccount):
  pass

my_banking = BankAccount(500)
my_investments = InvestmentAccount(750)
print(my_investments + my_banking)

#-------------------------------------------------

class Contacts:
  def __init__(self):
    self.view = 'list'
    self.contact_list = []
    self.choice = None
    self.index = None

  def display(self):
    while True:
      if self.view == 'list':
        self.show_list()
      elif self.view == 'info':
        self.show_info()
      elif self.view == 'add':
        print()
        self.add_contact()
      elif self.view == 'quit':
        print('\nClosing the contact list...\n')
        break

  def show_list(self):
    print()
    if len(self.contact_list) == 0:
      self.choice = input('(A)dd a new contact \n(Q)uit \n> ').lower()
    else:
      for index, contact in enumerate(self.contact_list):
        print(f"{index + 1}) {contact.first_name} {contact.last_name}")
      self.choice = input('\n(#) Select a name \n(A)dd a new contact\n(Q)uit \n> ').lower()
    self.handle_choice()

  def show_info(self):
    self.contact_list[self.index].display_info()
    self.choice = input('\n(C)ontact List \n(P)revious contact \n(N)ext contact \n(Q)uit \n> ').lower()
    self.handle_choice()

  def __add__(self, new_contact):
    self.contact_list.append(new_contact)

  def add_contact(self):
    self + Information()
    self.view = 'list'

  def handle_choice(self):
    if self.choice == 'q':
      self.view = 'quit'
    elif self.choice == 'a' and self.view == 'list':
      self.view = 'add'
    elif self.choice.isnumeric() and self.view == 'list':
      index = int(self.choice) - 1
      if index >= 0 and index < len(self.contact_list):
        self.index = index
        self.view = 'info'
    elif self.choice == 'c' and self.view == 'info':
      self.view = 'list'
    elif self.choice == 'n' and self.view == 'info':
      self.index = self.index + 1 if self.index + 1 < len(self.contact_list) else 0
    elif self.choice == 'p' and self.view == 'info':
      self.index = self.index - 1 if self.index - 1 >= 0 else len(self.contact_list) - 1

class Information:
  def __init__(self):
    self.first_name = input('Enter their first name: ')
    self.last_name = input('Enter their last name: ')
    self.personal_phone = input('Enter their personal phone number: ')
    self.personal_email = input('Enter their personal email address: ')
    self.work_phone = input('Enter their work phone number: ')
    self.work_email = input('Enter their work email address: ')
    self.title = input('Enter their work title: ')

  def display_info(self):
    print(f'\n{self.first_name} {self.last_name}')
    print(f'Personal phone number: {self.personal_phone}')
    print(f'Personal email address: {self.personal_email}')
    print(f'Work title: {self.title}')
    print(f'Work phone number: {self.work_phone}')
    print(f'Work email address: {self.work_email}')

contacts = Contacts()
contacts.display() 
