class Student:
    def __init__(self,ten,diem):
        self.ten=ten
        if diem>=0 and diem<=10:
            self.diem=diem
        else:
            self.diem=0