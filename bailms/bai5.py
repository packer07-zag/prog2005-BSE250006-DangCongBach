m=int(input("nhap hang: "))
n=int(input("nhap cot: "))
a=[]
for i in range(m):
    row=[]
    for j in range(n):
        row.append(x)
    a.append(row)
print("ma tran:")
for i in range(m):
    for j in range(n):
        print(a[i][j],end=" ")
    print()
h=int(input("chon hang: "))
for j in range(n):
    print(a[h-1][j],end=" ")
print()

c=int(input("chon cot: "))
for i in range(m):
    print(a[i][c-1])
max=a[0][0]
for i in range(m):
    for j in range(n):
        if a[i][j]>max:
            max=a[i][j]

print("max =",max)