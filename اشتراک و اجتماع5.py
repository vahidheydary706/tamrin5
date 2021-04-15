a = int(input())
b = set()

for i in range(a):
    b.add(input())

c = int(input())
d = set()

for i in range(a):
    d.add(input())
print( b, d)

print(b | d)

print(b.intersection(d))