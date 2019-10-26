math = float(input("Enter math grade:"))
physics = float(input("Enter physics grade:"))
chemistry = float(input("Enter a chemistry grade:"))
totalgrade = math + physics + chemistry

if math < 35:
    print("Student failed the exam")
elif physics < 35:
    print("Student failed the exam")
elif chemistry < 35:
    print("Student failed the exam")
else:
    print("Student passed the exam")
    print("Total score is:",totalgrade)
    average = round(totalgrade/3,2)
    print("Average score is:",average)
    if average <= 59:
        print("Grade is C")
    elif average <= 69:
        print("Grade is B")
    else:
        print("Grade is A")

