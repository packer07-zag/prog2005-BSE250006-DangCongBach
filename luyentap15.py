# Bài 1
a=int(input())
b=int(input())
print(a+b)
print(a-b)
print(a*b)
print(a/b if b!=0 else "Khong chia duoc")

# Bài 2
def greet(name="Student"):
    print("Hello,",name+"!")

greet()
greet("Anh")

# Bài 3
def gt(n):
    if n==0 or n==1: return 1
    return n*gt(n-1)

n=int(input())
print(gt(n))

# Bài 4
a=float(input())
b=float(input())
c=float(input())
tb=(a+b+c)/3
print(tb)

if tb>=8: print("Gioi")
elif tb>=6.5: print("Kha")
elif tb>=5: print("Trung binh")
else: print("Yeu")

# Bài 5
def count_vowels(s):
    c=0
    for i in s.lower():
        if i in "aeiou":
            c+=1
    return c

s=input()
print(count_vowels(s))

# Bài 6
m=["do","xanh","vang","tim","den"]
x=input()
if x in m: m.remove(x)
print(m)

# Bài 7
d={"An":8,"Binh":7,"Cuong":9}
print(sum(d.values())/len(d))

# Bài 8
class Product:
    def __init__(self,p):
        self._p=p

    def get_price(self):
        return self._p

    def set_price(self,p):
        if p<0:
            print("Loi")
        else:
            self._p=p
sp=Product(input())
print(sp.get_price())
sp.set_price(input())