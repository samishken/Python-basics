# print all numbers except the one that are divisible by 3
x=0
while x < 20:
    x+=1
    if x%3 == 0:
        continue
    print(x)