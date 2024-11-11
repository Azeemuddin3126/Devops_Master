# Parent Class 1
class Parent1:
    def identify(self):
        return "This method is called from Parent1"

# Parent Class 2
class Parent2:
    def identify(self):
        return "This method is called from Parent2"

# Child Class that inherits from both Parent1 and Parent2
class Child(Parent2, Parent1):
    def identify(self):
        return "This method is called from Child"

    def identify2(self):
        return super().identify()  # Calls identify() from Parent2

# Create an instance of Child
child_object = Child()

# Output the results
print(child_object.identify())   # This will call the Child's identify method
print(child_object.identify2())  # This will call the identify method from Parent2 using super()
