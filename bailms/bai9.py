"""
# Bài 9
Tạo lớp `Animal` có thuộc tính name và phương thức sound() 
Tạo lớp con `Dog` kế thừa và ghi đè phương thức `sound()` 
(Mô phỏng phương thức sound() bằng hàm print() 
in ra một tiếng bất kỳ).
Dùng super trong lớp con để khai khởi tạo tên
Chạy thử bằng cách tạo một đối tượng của lớp Dog
"""
class Animal:
    def __init__(self,name):
        self.name=name
    def sound(self):
        print("Animal sound")
class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)
    def sound(self):
        print("Gâu gâu")
name=input("Nhập tên chó: ")
d=Dog(name)
print("Tên:",d.name)
d.sound()