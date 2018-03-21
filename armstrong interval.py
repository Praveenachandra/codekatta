a=int(input(""))
b=int(input(""))
for i in range(a,b+1):
    order=len(str(i))
    sum=0
    temp=i
    while(temp>0):
        digit=temp%10
        sum+=digit**order
        temp//=10
    if (i==sum):
        print i
else:
    print("none")
