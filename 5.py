#  Write a program to show the grade obtained by a student after he/she enters their total mark percentage.
# Program should accept an input from the user and display their grade as follows



mark=float(input("enter the mark"))
if mark<50:
    print("fail")
elif mark<=59:
    print("e")
elif mark<=69:
    print("d")
elif mark<=79:
    print("c")
elif mark<=89:
    print("b")
elif mark<=100:
    print("a")
else:
    print("please enter correct mark")


