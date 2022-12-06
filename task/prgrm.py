x=int(input("enter the value of x:"))
y=int(input("enter the value of y:"))
z=x*y
test=list(range(1,z+1))
for i in range(1,len(test)):
    if i%3==0:
        if i==z:
            pass
        else:
            test[i-1],test[i]=test[i],test[i-1]
m=[]
n=[]
o=[]
for i in range(0,len(test)):
    if i%3==0:
        m.append(test[i])
    elif i%3==1:
        n.append(test[i])
    else:
        o.append(test[i])
print(m)
print(n)
print(o)
