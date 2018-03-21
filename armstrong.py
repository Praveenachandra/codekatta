a=int(input(""))
temp=a
sum=0
order=len(str(a))
while (temp>0):
    digit=temp%10
    sum+=digit**order
    temp//=10
if (sum==a):
    print (a,"is a armstrong number")
else:
    print(a,"is not an armstrong number")
