class A:
    def __init__(self):
        self.a = 5

    def talk(self):
        print(self.a)



class B(A):
    def __init__(self):
        super().__init__(self)
        self.b = 6

    def talk(self):
        print(self.b, self.a)

B().talk()