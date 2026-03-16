"""
bai3
**Yêu cầu**: Viết chương trình chuẩn hóa tên người dùng: 
Loại bỏ khoảng trắng thừa ở hai đầu, giữa các từ chỉ để lại một 
khoảng trắng và viết hoa chữ cái đầu mỗi từ. 
Ví dụ: " nguyêN văn A " -> "Nguyễn Văn A".
"""
name=input("Nhập tên: ").strip().split()
tên=" ".join(name).title()
print(tên)