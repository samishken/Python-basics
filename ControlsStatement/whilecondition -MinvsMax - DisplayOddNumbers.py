# Enter two numbers Min & Max
# Display all odd number between the min & max

x=int(input("Enter min number"))
y=int(input("Enter max number"))

i=x
# if min number is even then add 1 to make it odd.
# start with odd
if i % 2 == 0: i=x+1

# loop from min to max
while i <= y:
    print(i)
    i+=2

