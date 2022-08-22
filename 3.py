# Write a program to find the simple interest.
# Program should accept 3 inputs from the user and calculate simple interest for the given inputs. Formula: SI=(P*R*n)/100)

p=int(input("enter the principal amount"))
r=float(input("enter the interest rate"))
n=float(input("enter the number of year"))
si=((p*r*n)/100)
print(si)