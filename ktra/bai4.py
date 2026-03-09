n=int(input())
a=list(map(int,input().split()))
for i in range(0,n):
    for j in range(i+1,n):
        if a[j]>a[i]:
            s=a[j]
            a[j]=a[i]
            a[i]=s
    print(a)
