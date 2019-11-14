"""
lst=[] will store the results
each number in range 1-11 will be assigned to x
append = add element to the list.
multiply x**3
print(lst) = result
"""

lst=[]
for x in range(1,11):
    lst.append(x**3)
print(lst)

print("check for similar results")
lst=[]
lst=[x**3 for x in range(1,11)]
print(lst)

