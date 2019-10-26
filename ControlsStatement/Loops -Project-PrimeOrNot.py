"""
Figure out if a given number is prime or not.
Prime numbers are the natural numbers greater
than one that are not products of two smaller
natural numbers.
"""
n=int(input("Please enter a number: "))
primeFlag = True  #setting all number to be prime by default.

for i in range(2,n-1):
    if n%i==0:
        primeFlag = False
if(primeFlag):
    print(n,"is a Prime Number")
else:
    print(n,"is not a Prime Number")


















