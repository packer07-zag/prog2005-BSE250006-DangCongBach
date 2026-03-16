"""# Bài 4
**Yêu cầu**: Xử lý chuỗi với các hàm cơ bản. 
Viết chương trình cho phép nhập một chuỗi. 
Chương trình phải xuất ra:
- Số lượng chữ cái in hoa
- Số lượng chữ cái in thường
- Số lượng chữ số
- Số lượng ký tự đặc biệt
- Số lượng ký tự khoảng trắng
- Số lượng nguyên âm
- Số lượng phụ âm
"""
s=input("Nhập chuỗi: ")
hoa=thuong=so=ktdb=space=ngam=phuam=0
na="aeiouAEIOU"
for c in s:
    if 'A'<=c<='Z':
        hoa+=1
    elif 'a'<=c<='z':
        thuong+=1
    if '0'<=c<='9':
        so+=1
    if c==" ":
        space+=1
    if not ('a'<= c <='z' or '0'<=c<='9' or c==" " or 'A'<=c<='Z'):
        ktdb+=1
    if c in na:
        ngam+=1
    elif not (c in na or '0'<=c<='9'or c==" "):
        phuam+=1
print("Chữ hoa:",hoa)
print("Chữ thường:",thuong)
print("Chữ số:",so)
print("Ký tự đặc biệt:",ktdb)
print("Khoảng trắng:",space)
print("Nguyên âm:",ngam)
print("Phụ âm:",phuam)