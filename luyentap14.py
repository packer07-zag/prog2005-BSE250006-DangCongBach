# ===== Bài 1 =====
PI=3.14
r=float(input())
cv=2*PI*r
print(cv)
# ===== Bài 2 =====
a=[]
for i in range(5):
    name=input(f"Nhap ten thu {i+1}: ")
    a.append(name)
print(a)
del a[1]
print("Sau khi xoa vi tri thu 2:",a)
# ===== Bài 3 =====
def ktra(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
arr=list(map(int,input().split()))
le=[]
for i in range(n):
    if arr[i]%2!=0:
        le.append(arr[i])
print("So le:",*le,"| So luong:",len(le))

nt=[]
for i in range(n):
    if ktra(arr[i]):
        nt.append(arr[i])
print("So nguyen to:",*nt)
# ===== Bài 4 =====
class Book:
    def __init__(self,name,price):
        self.__name=name
        self.__price=price

    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name=name

    def get_price(self):
        return self.__price
    def set_price(self,price):
        self.__price=price

b=Book("Book 1",30000)
print("Price:",b.get_price())
# ===== Bài 5 =====
f=open("book.txt","w",encoding="utf-8")
f.write("Book 1;30000\n")
f.write("Book 2;50000\n")
f.write("Book 3;100000\n")
f.write("Tong;900000")
f.close()