s="You are welcome"
print(s)

s1="""You are
the best 
footballer
"""
print(s1)

#Indexing
print(s*3)

#length
print(len(s1))
print(len(s))

#slicing a string
# You a
print(s[0:5])
# You are welcome
print(s[0:])

#negative numbers
# om
print(s[-3:-1])

#steps of 2.  jump 2
# "Y u a e w"
# Yuaew
print(s[0:9:2])
# Without stps of two
# You are w
print(s[0:9])

#Reverse order
#print entire reverse order (emoclew era uoY)
print(s[15::-1])
print(s[::-1])
# only print welcome (emoclew)
print(s[15:7:-1])

#strip out spaces
j="   You are welcome   "
print(j.strip())
# remove the space from left side
print(j.lstrip())
# remove the spaces from right side
print(j.rstrip())




