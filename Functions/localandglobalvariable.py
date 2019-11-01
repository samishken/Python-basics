x=123 #GlobalVariable

def display():
    y=678 #LocalVariable
    print(y)
    print(globals()['x'])

print(x)
display()