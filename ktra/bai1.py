a,b,c=list(map(float,input().split()))
print(max(a,b,c),min(a,b,c))
d=b*b-4*a*c
if d>0:
    x1=(-b+d**0.5)/(2*a)
    x2=(-b-d**0.5)/(2*a)
    print(x1,x2)
elif d==0:
    x=-b/(2*a)
    print(x)
else:
    print("vo nghiem")
