lst=[10, 20, 'Liverpool', -10, 30.5]
# Entire list
print(lst)
# print third index
print(lst[3])
# print index from 3 to 5
print(lst[3:5])
# print the list four times
print(lst*4)
# length
print(len(lst))


# add element
lst.append(40)
print(lst)

# remove element
lst.remove('Liverpool')   # case sensitive
print(lst)

#delete element
del(lst[1])
print(lst)

# max and min element in the list
print(max(lst))
print(min(lst))

# Insert
# Insert 99 at index 3
# outcome [10, -10, 30.5, 99, 40]
lst.insert(3, 99)
print(lst)

# Sort
   # asc
lst.sort()
print(lst)
   # desc
lst.sort(reverse=True)
print(lst)

#clear all elements
lst.clear()
print(lst)

