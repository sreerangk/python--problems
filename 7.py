# Write a program to print the multiplication table of given numbers.
# Accept an input from the user and display its multiplication table
num=int(input("enter the number "))

for i in range(1,11):
    print(num,'x',i,'=',num*i)
