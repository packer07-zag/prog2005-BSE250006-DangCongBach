
"""
# Bài 8
Tạo class Vector, có thuộc tính x và y. 
Nạp chồng toán tử add (+) cho lớp Vector
Chạy ví dụ.
"""
class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y)
    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"
x1=int(input("x1: "))
y1=int(input("y1: "))
x2=int(input("x2: "))
y2=int(input("y2: "))
v1=Vector(x1,y1)
v2=Vector(x2,y2)
v3=v1+v2
print(v3)