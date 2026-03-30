# ===== CÂU 1 =====
def cau1():
    n = int(input("Nhập số: "))
    if n < 0:
        print("Lỗi: số âm")
    else:
        print("Phần dư khi chia cho 2 là:", n % 2)


# ===== CÂU 2 =====
def cau2():
    s = input("Nhập chuỗi: ")
    print("Chiều dài chuỗi:", len(s))
    print("Chuỗi viết hoa:", s.upper())


# ===== CÂU 3 =====
def cau3():
    i = 1
    tong = 0

    while i <= 30:
        if i % 2 != 0:
            print(i)
            tong += i
        i += 1

    print("Tổng các số lẻ là:", tong)


# ===== CÂU 4 =====
def tong(n):
    if n == 1:
        return 1
    return n + tong(n - 1)

def cau4():
    n = int(input("Nhập n: "))
    print("Tổng là:", tong(n))


# ===== CÂU 5 =====
class Flower:
    def __init__(self, color):
        self._color = color

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color


def cau5():
    f1 = Flower("Red")
    print("Màu ban đầu:", f1.get_color())
    f1.set_color("Yellow")
    print("Màu sau khi đổi:", f1.get_color())


# ===== CÂU 6 =====
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


def cau6():
    a = [5, 2, 8, 1, 3]
    print("Mảng sau khi sắp xếp:", selection_sort(a))


# ===== MENU CHỌN BÀI =====
while True:
    print("\n===== MENU =====")
    print("1. Câu 1")
    print("2. Câu 2")
    print("3. Câu 3")
    print("4. Câu 4")
    print("5. Câu 5")
    print("6. Câu 6")
    print("0. Thoát")

    chon = int(input("Chọn bài: "))

    if chon == 1:
        cau1()
    elif chon == 2:
        cau2()
    elif chon == 3:
        cau3()
    elif chon == 4:
        cau4()
    elif chon == 5:
        cau5()
    elif chon == 6:
        cau6()
    elif chon == 0:
        break
    else:
        print("lỗi!")