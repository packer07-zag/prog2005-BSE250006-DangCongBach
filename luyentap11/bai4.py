a=list(map(int,input().split()))

# them phan tu
x=int(input())
a.append(x)

# dem k
k=int(input())
print(a.count(k))

# tong so nguyen to
def nt(n):
    if n<2: return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0: return False
    return True

s=0
for i in a:
    if nt(i):
        s+=i
print(s)

# sap xep
a.sort()
print(a)

# xoa danh sach
a.clear()
print(a)