erro




import numpy as np 
a=[]
b=[]
c=[]
row =int(input("enter therow"))
col=int(input("eter the columns"))
for i in range(row):
    row=[]
    for j in range(col):
        l1=int(input())
        row.append(l1)
    a.append(row)
print("display array in metrix form")
for i in range(row):
    for j in range(col):
        print(a[i][j],end="")
for i in range(row):
    for j in range(col):
        print(b[i][j],end="")
    print()
a = np.array(a)
b= np.array(b)
c= np.array(a+b)
print("display sun of 2 array")
for i in range(row):
    for j in range(col):
        print(c[i][j],end="")
    print()
