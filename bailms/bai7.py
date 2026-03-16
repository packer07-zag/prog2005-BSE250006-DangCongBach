"""
# Bài 7
Tạo đối tượng Person có thuộc tính name và age, 
có class method tạo đối tượng Person từ chuỗi "name-age" 
(ví dụ: "Nam-20").
"""
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def create(cls,s):
        name,age=s.split("-")
        return cls(name,int(age))
s=input("Nhập dạng name-age: ")
p=Person.create(s)
print("Name:",p.name)
print("Age:",p.age)