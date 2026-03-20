class A:
    def __init__(self, x):
        if x < 0:
            raise ValueError
        self.x = x
    def __str__(self):
        return str(self.x)
    def __eq__(self, o):
        return self.x == o.x
    @classmethod
    def cl(cls):
        return "A"
    @staticmethod
    def st(x):
        return x > 0
class B(A):
    def __init__(self, x, y):
        super().__init__(x)
        if y < 0:
            raise ValueError
        self.y = y
    def __str__(self):
        return str(self.x) + " " + str(self.y)
a = A(5)
b = B(3,4)
print(a)
print(b)
print(a == A(5))
print(A.cl())
print(A.st(2))