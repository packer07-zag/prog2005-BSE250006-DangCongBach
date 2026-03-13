n=int(input())
d={}
for i in range(n):
    k=input()
    v=input()
    d[k]=v

x=input()
if x in d: print("Ton tai")
else: print("Khong ton tai")