class Hoa:
    def __init__(self,ten,mau):
        self.ten=ten
        self.mau=mau

ten=input()
mau=input()

h=Hoa(ten,mau)
print(h.ten,h.mau)