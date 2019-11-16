class Car:
    #outer class
    def __init__(self,make,year):
        self.make=make
        self.year=year
    #inner class
    class Engine:
        def __init__(self,number):
            self.number=number
        def start(self):
            print("Engine Started")

#inorder to access the inner class
#first create the instance of the outer class
c = Car("BMW",2017)
e = c.Engine(123)
e.start()
