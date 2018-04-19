s=raw_input("")
s=s.lower()
count=0
for i in (s):
    if i in ('a','e','i','o','u'):
        count=count+1
    else:
        count=count
if(count>0):
    print "yes"
else:
    print "no"
