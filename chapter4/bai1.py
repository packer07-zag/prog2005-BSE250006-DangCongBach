def f(t):
    s=0
    mx=t[0]
    mn=t[0]
    for i in t:
        s+=i
        if i>mx: mx=i
        if i<mn: mn=i
    print("Tong:",s)
    print("Max:",mx)
    print("Min:",mn)

t=tuple(map(int,input().split()))
f(t)