n = int(input())
if n<2:
    print("No")
else:
    ktra = True
    for i in range(2, int(n**0.5)+1):
        if n % i==0:
            ktra=False
            break
    if ktra:
        print("Yes")
    else:
        print("No")