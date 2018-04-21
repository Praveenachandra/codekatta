n=raw_input("")
k=raw_input("")
l=raw_input("")
l=map(int,l.split(" "))
count=0
for i in l:
    if(i==int(k)):
        count=count+1
print count
