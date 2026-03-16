"""
# Bài 11
Tạo class method của class SinhVien 
đếm số đối tượng được tạo ra.
Chạy ví dụ
"""
class SinhVien:
    dem=0
    def __init__(self,ten):
        self.ten=ten
        SinhVien.dem+=1
    @classmethod
    def so_luong(cls):
        return cls.dem
n=int(input("Nhập số sinh viên: "))
for i in range(n):
    ten=input("Tên SV: ")
    sv=SinhVien(ten)
print("Số sinh viên đã tạo:",SinhVien.so_luong())