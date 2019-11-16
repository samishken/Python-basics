"""
def __init__(self) is a Constructor

A constructor is a special kind of method that
Python calls when it instantiates
an object using the definitions
found in your class. Python relies on the
constructor to perform tasks such as
initializing (assigning values to) any
instance variables that the object
will need when it starts.

the INIT method constructs the object of the class.
"""

class Product:
    def __init__(self):
        self.name = 'IPhone'
        self.description = 'Its Awesome'
        self.price = 700

p1 = Product()
print("p1")
print(p1.name)
print(p1.description)
print(p1.price)

p2 = Product()
print("p2      ******")
print(p2.name)
print(p2.description)
print(p2.price)

"""
- class = Product
- init method = construct the object of class Product
- self = address or memory location of the current object will be assigned
- assigned fields and provide values to the fields
- p1 = Product() create object of the class
- print(p1.name) object variable.field name

"""

