"""
Tuple cannot be modified like a list.
We can't use the following methods in Tuple
append, extend, insert, remove, clear
"""

tpl=(40, 50, 50, 'xyz')
print(tpl)

tpl=(40,)
# with comma its considered as tuple
print(type(tpl))
tpl=(40)
# without comma its considered as integer
print(type(tpl))

tpl=(40, 50, 40, 'xyz')
print(tpl)   # print all elements in the tuple
print(tpl[3])  # give me the element that's is the third index
print(tpl*3) # multiply the tuple 3 times
print(tpl.count(40))  # how many 40 inside a tuple
print(tpl.index('xyz'))  # what's the index number of that element

lst=[67, 54, 'xyz']
print(type(lst))

tpl1=tuple(lst)
print(type(tpl1))
