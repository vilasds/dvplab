num=int(input("enter a number"))
val=str(num)
rev=val[::-1]
if(val==rev):
    print("pal")
else:
    print("not pal")
for i in range(10):
    if(val.count(str(i))>0):
        print(str(i),"appears",val.count(str(i)),"times")