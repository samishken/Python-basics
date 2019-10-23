s={10,20,30, 'xyz', 10, 20, 10}
print(s)  # outcome do not include duplicates
print(type(s)) # outcome <class 'set'>

# Add
s.update([88, 99])  # will add this new element
print(s)
print(type(s))

#Remove
s.remove(30)
print(s)

# Prevent from Update and Remove
f=frozenset(s)
f.update(30) # not allowed after frozenset
f.remove(10) # ERROR after frozenset

# 'set' object does not support indexing

