"""
Static field and static method


Count the number of Objects
of a particular class
that are being created
and display the count

"""

class ObjectCounter:
    """
    This field will store the number of objects.

    Every time an object is created this will
    be incremented start with zero.
    """
    #static field
    numberOfObjects = 0

    def __init__(self):
        ObjectCounter.numberOfObjects+=1

    #static method
    #decorator
    @staticmethod
    def displayCount():
        print(ObjectCounter.numberOfObjects)

o1= ObjectCounter()
o2= ObjectCounter()
o3= ObjectCounter()

ObjectCounter.displayCount()