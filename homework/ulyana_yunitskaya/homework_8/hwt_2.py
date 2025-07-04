def fibo(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


count = 1
for number in fibo(100000):
    if count == 5:
        print(number)
    if count == 200:
        print(number)
    if count == 1000:
        print(number)
    if count == 100000:
        print(number)
        break
    count += 1
