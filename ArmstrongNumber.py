n = int(input("enter the number"))
s=0
m=n
while(n>0):
    r=r%10
    s = s + r*r*r
    n= n//10
if(m==s):
    print("Armstrong nunber")
else:
    print("better luck next time")
    