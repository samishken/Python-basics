"""
Part 1: Access public fields
Part 2: Access private fields
Part 3: Use Name Mangling to access private fields
"""
# Without private data
class Student:

    def __init__(self):
        self.id=123
        self.name="John"

s = Student()
print(s.name)
print(s.id)

print("")

"""
Make the field private
create functions 
to access the private fields
"""
class Student:

    def __init__(self):
        self.__id=123
        self.__name="John"

    def dispaly(self):
        print(self.__id)
        print(self.__name)

s = Student()
s.dispaly()

print("")
"""
Part III
Name mangling
"""
s = Student()
print(s._Student__id)
print(s._Student__name)
