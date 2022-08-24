# Write a program to find the sum of all the odd numbers for a given limit
# Program should accept an input as limit from the user and display the sum of all the odd numbers within that limit



limit=int(input("enter a limit "))
sum=0
for i in range(limit):
    if i%2==1:
        sum=sum+i
        print(i,'+ ',end="")
print('=',sum)