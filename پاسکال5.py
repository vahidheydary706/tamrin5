a = int(input('radif: '))
p = [[1 for i in range(a)]for j in range(a)]


for i in range(a):
    for j in range(1 , i):
                p[i][j] = p[i - 1][j - 1]+p[i - 1][j]



for i in range(a):
    for j in range(i + 1):
        print(p[i][j], end=" ")
    print(" ")