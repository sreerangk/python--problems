def count(lst):
    evn=0
    odd=0
    for i in lst:
        if i%2==0:
            evn+=1
        else:
            odd+=1
    return evn,odd



lst=[]
n=int(input("enter size of list"))

for i in range(0,n):
    l=int(input("enter the  number"))
    lst.append(l)
x,y=count(lst)
print("even :{} and odd : {}".format(x,y))
print("even",x,"odd",y) #another method printing