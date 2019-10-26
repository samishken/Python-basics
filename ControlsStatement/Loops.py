# input number
# display number up to that number
# skip multiples of 10 #continue
# stop if the number > 100 #break

x=int(input("Please enter a number: "))
r = range(0, x + 1)
for i in r:
    if i > 100: break
    if i % 10 == 0: continue
    print(i)