b=list(map(int,input().split()))
s=0
for i in b:
    if i%2==0:
        print(i,end=" ")
        s+=i

print("\nTong:",s)