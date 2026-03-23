n=int(input())
m=int(input())

a=[]
b=[]

for i in range(n):
    a.append(list(map(int,input().split())))

for i in range(n):
    b.append(list(map(int,input().split())))

c=[]
for i in range(n):
    row=[]
    for j in range(m):
        row.append(a[i][j]+b[i][j])
    c.append(row)

for i in c:
    print(*i)