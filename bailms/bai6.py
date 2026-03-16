"""
# Bài 6
Tạo lớp `Product` với 
- thuộc tính `_price` có thể được khởi tạo qua constructor 
- getter price
- setter price có kiểm tra giá trị truyền vào `> 0`.
- Viết hàm `__str__` để in thông tin price của product.
Khởi tại một đối tượng Product và in ra giá.
"""
class Product:
    def __init__(self,price):
        self._price=price
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self,value):
        if value>0:
            self._price=value
    def __str__(self):
        return "Price: "+str(self._price)

p=float(input("Nhập giá: "))
sp=Product(p)
print(sp)