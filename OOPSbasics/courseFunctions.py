"""
Parameterized Constructor
Instance method
"""
class Course:

    def __init__(self,name,ratings):
        self.name = name
        self.rate = ratings

    def average(self):
        numberOfRatings = len(self.rate)
        average = sum(self.rate)/numberOfRatings
        print("Average Ratings For ",self.name," Is ",average)


print("")
c1 = Course('Java Course', [1,3,3,4,5])
print("^^^ COURSE ONE NAME AND RATINGS^^^")
print("Course name ",c1.name)
print("Course ratings ",c1.rate)
c1.average()
print("")

c2 = Course('Python Course', [5,5,3,4,5])

print("^^^ COURSE TWO NAME AND RATINGS^^^")
print("Course name ",c2.name)
print("Course ratings ",c2.rate)
c2.average()