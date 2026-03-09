n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
print()
for i in range(1,n):
    for j in range(1,2*n):
        if j==n-i+1 or j==n+i-1 or i==n:
            print("*",end="")
        else:
            print(" ",end="")
    print()
for j in range(1,2*n+1,2):
    print("*",end=" ")
        