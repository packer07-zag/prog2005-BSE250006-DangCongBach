"""
# Bài 10
Tạo class SinhVien có thuộc tính điểm
Nạp chồng toán tử `==` để so sánh hai sinh viên theo điểm.
Chạy thử.
"""
class SinhVien:
    def __init__(self,diem):
        self.diem=diem
    def __eq__(self,other):
        return self.diem==other.diem
d1=float(input("Điểm SV1: "))
d2=float(input("Điểm SV2: "))
sv1=SinhVien(d1)
sv2=SinhVien(d2)
if sv1==sv2:
    print("Hai sinh viên có điểm bằng nhau")
else:
    print("Hai sinh viên có điểm khác nhau")