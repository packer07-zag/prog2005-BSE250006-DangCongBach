print("nhập số trong khoảng 1 đến 9")
while True:
    a=int(input())
    if 0<a<10:
        break
    print(" nhập sai , biết đọc chữ ko ")
for i in range(1,11):
    print(f"{i} * {a} = {i*a}")