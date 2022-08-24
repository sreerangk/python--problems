# Write a program to interchange the values of two arrays.
#swap two elements in list

a=[]
b=[]
n=int(input("Number of elements in 1st array:"))
n2=int(input("Number of elements in 2st array:"))
for i in range(0,n):
   l=int(input("1st array elements"))
   a.append(l)
print("first array is ",a)
for i in range(0,n2):
   l2=int(input("2nd array elements"))
   b.append(l2)
print("second array is ",b)

tem=a
a=b
b=tem
print("array 1\n",a)
print("array 2\n",b)