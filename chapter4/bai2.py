n=int(input())
d={}
for i in range(n):
    ten=input()
    diem=float(input())
    d[ten]=diem
s=0
for i in d:
    s+=d[i]
print("Diem trung binh:",s/n)