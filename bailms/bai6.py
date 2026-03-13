s=input("nhap chuoi: ")
a=s.split(";")
chan=0
am=0
nt=0
tong=0
for i in range(len(a)):
    x=int(a[i])
    print(x)
    tong=tong+x
    if x%2==0:
        chan=chan+1
    if x<0:
        am=am+1
    if x>1:
        ok=True
        for j in range(2,x):
            if x%j==0:
                ok=False
        if ok:
            nt=nt+1
print("so chan:",chan)
print("so am:",am)
print("so nguyen to:",nt)
print("trung binh:",tong/len(a))