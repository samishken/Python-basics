"""
create instance methods
that can access variables

"""


class Product:
    def __init__(self):
        self.name = 'IPhone'
        self.description = 'Its Awesome'
        self.price = 700

    def display(self):
        print(self.name)
        print(self.price)
        print(self.description)

print("p1")
p1 = Product()
p1.display()

print("")

print("p2")
p2 = Product()
p2.display()