dict1={1:"John", 2:"Bob", 3:"Bill"}
#keys = 1,2,2
#values of keys = John, Bob, Bill
print(dict1)

print(dict1.values())
print(dict1.items())

#list only keys
k=dict1.keys()
for i in k:print(i)

# print only values
v=dict1.values()
for i in v:print(i)

#pass key
print(dict1[3])

#Delete
# delete one of the keys
del dict1[3]
print(dict1)