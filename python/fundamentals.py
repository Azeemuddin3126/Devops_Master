#----------------------------------
#printing
#-----------------------------------
print("hello world")
print("hello", end='/n')#"", "\t", "\!"
print("world")

#----------------------------------
#comments
#-----------------------------------
#comments
'''
multi line
'''

#----------------------------------
#Data Types
#-----------------------------------
my_variable = "Hello world"
print(my_variable)
my_variable = "Goodbye world"
print(my_variable)

string_variable = "This is a string"
second_string = 'This is a string also'
print(string_variable)
print(second_string)

boolean_variable = True
print(boolean_variable)

integer_variable = 50 #5,000 #050
float_variable=50.0, 50., .001
print(integer_variable,float_variable)

#----------------------------------
# Arthematcis Operations
#-----------------------------------
 
 #Operations
a=20.0
b=10
print(a+b)
print(a-b)
print(a/b)
print(a//b)# retunrs floor no float values for whole numbers
print(a*b)
print(3*"hello")
print(a**b)
print(a%b)

 #incremenst
a = 0
b = 0
a = a + 1
b += -1
print(a)
print(b)

 #Type casting
a = 3
print(type(a))
a = str(a)
print(type(a))
a = 5
b = "3"
print(a + int(b))

 #String Concatenation
a = "This is an "
b = "example string"
c = a + b
print(c)

a = "This is an "
b = "example string"
a += b
print(a)
 
 #order of OPs
a = 2
b = 3
c = 4
result = 3 * a ** 3 / (b + 5) + c
print(result) #PEMDAS

#----------------------------------
# Boolean Operations
#-----------------------------------

a=5
b=5
print(a==b)
print(a!=b)
print(a<b)
print(a>b)
print(a<=b)

a = True
b = True
c = False
print(a and c and a and b and a) #AND--for True ALL must if 1 false all become false
print(a or c or c or c or c) #OR---If only one is true, then all is true. To be false, all must be false.
print(not (True and False)) #NOT---Opposite
print(not True and False)
print(not not True)
print(3<4 and 1>0)
print(10>6 or 6<5)
print(10>12 or 20>4)










