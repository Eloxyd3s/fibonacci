base = "0 1 "
a, b = 0, 1
data = 0
n = int(input("amount of numbers?"))
while data <= n:
    c = a + b
    base += str(c)+" "
    data += 1
    a = b
    b = c

print(base)