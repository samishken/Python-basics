"""
Parameterized Constructor
"""
class Course:

    def __init__(self,name,ratings):
        self.name = name
        self.rate = ratings
print("")
c1 = Course('Java Course', [1,2,3,4,5])
print("^^^ COURSE ONE NAME AND RATINGS^^^")
print("Course name ",c1.name)
print("Course ratings ",c1.rate)
print("")

c2 = Course('Python Course', [1,2,3,4,5])

print("^^^ COURSE TWO NAME AND RATINGS^^^")
print("Course name ",c2.name)
print("Course ratings ",c2.rate)











"""
- class = Product
- init method = construct the object of class Product
- self = address or memory location of the current object will be assigned
- assigned fields and provide values to the fields
- p1 = Product() create object of the class
- print(p1.name) object variable.field name

"""