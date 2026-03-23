x=input()

l=0
r=len(a)-1
kq=-1

while l<=r:
    m=(l+r)//2
    if a[m]==x:
        kq=m
        break
    elif len(a[m])<len(x):
        r=m-1
    else:
        l=m+1

if kq==-1:
    print("Khong tim thay")
else:
    print("Vi tri:",kq)