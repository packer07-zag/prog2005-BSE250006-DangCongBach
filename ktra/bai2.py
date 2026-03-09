def kt(n):
    if n<2:
        return False
    if n%2==0 and n!=2:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True
for i in range(111,16,-2):
    print(i,end=' ')
print(' ')
for i in range(17,112):
    if kt(i):
        print(i,end=' ')
    