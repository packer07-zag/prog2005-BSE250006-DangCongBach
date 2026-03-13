class Product:
    def __init__(self,p):
        self._price=p
    def get_price(self):
        return self._price
    def set_price(self,p):
        if p>0: self._price=p
    def __str__(self):
        return str(self._price)

p=int(input())
sp=Product(p)

print(sp)

m=int(input())
sp.set_price(m)

print(sp)