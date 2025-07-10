def fib(n):
    if n <= 1:
        return n
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(1, n+1):
        n = a + b
        print(n)
        a = b
        b = n
print(fib(10))
        