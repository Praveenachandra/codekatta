a=input("")
dig=0
sum=0
while(a>0):
    dig=a%10
    a//=10
    sum=sum+dig
print sum
