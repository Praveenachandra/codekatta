num=int(input(""))
fac=1
if(num<0):
    print "no factorial"
elif(num==0):
    print " the factorial is 1"
else:
    for i in range (1,num+1):
        fac=fac*i
        print fac
