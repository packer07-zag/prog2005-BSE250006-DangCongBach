while True:
    chon = input()
    if chon == "1":
        s = input()
        c = input()
        print(s.count(c))
    elif chon == "2":
        def gt(n):
            if n <= 1:
                return 1
            return n * gt(n-1)
        print(gt(int(input())))
    elif chon == "0":
        break