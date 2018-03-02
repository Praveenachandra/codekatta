num=int(input(""))
fac=1
temp=num
if temp<0:
    print "no factorial"
elif temp==0:
    print "the factorial is 1"
else:
    for i in range(1,temp+1):
        fac=fac*i
        print fac
