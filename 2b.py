def b2d(n):
    return int(n,2)
def o2h(n):
    return hex(int(n,8))
bnum=input("Enter binary no:")
dnum=b2d(bnum)
print("Decimal num=",dnum)
onum=input("Enter octal num:")
hnum=o2h(onum)
print("hexadecimal num=",hnum)