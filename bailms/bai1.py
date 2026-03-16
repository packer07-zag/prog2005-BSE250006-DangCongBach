"""
# Bài 1
**Yêu cầu**: Tính BMI (Chỉ số khối cơ thể)
Viết một chương trình tính và hiển thị BMI:
- Nhập cân nặng ('kg') và chiều cao (`m`)
- Công thức: `BMI = weight / (height * height)`, sử dụng kiểu float và các toán tử số học.
- Hiển thị BMI làm tròn 2 chữ số thập phân
- Ví dụ: nếu `weight = 60kg` và height = `1.65m → BMI ≈ 22.04`
"""
weight=float(input("Nhập cân nặng :"))
height=float(input("Nhập chiều cao :"))
BMI = weight / (height * height)
BMI=round(BMI,2)
print(BMI)
