# Python program to print all
# prime number in an interval
a = range(3,1000)
for x in range(len(a)):
    # If num is divisible by any number
    # between 2 and val, it is not prime
    if x > 1:
        for y in range(2, x):
            if x%y== 0:
                break
        else:
            print(x)
