
a = int(input("tayp namber:"))
for i in range(a):
    b = 1
    c = 0
    list =list()

    if a < 0:
        print("wrong")
    else:
        for i in range(a):
            list.append(c)
            t = b + c
            b = c
            c = t
        print(tuple(list))
    