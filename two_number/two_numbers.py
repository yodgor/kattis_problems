line = input()
a, b = line.split()
a = int(a)
b = int(b)

if (a >= 0 and a <= 1000000) and (b>=0 and b <=1000000):
    print(a+b)
