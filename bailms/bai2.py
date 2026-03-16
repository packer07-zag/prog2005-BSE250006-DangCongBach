"""
# Bài 2
**Yêu cầu**: Yêu cầu người dùng nhập vào một số và tính tổng các chữ số của số đó.
"""
def tcs(n):
    t=0
    while n%10!=0:
        t+=n%10
        n//=10
    return t
n=int(input("nhập số:"))
print(tcs(n))