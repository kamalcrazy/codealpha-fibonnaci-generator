def fibonacci(k):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(k):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence
n = int(input("Enter an integer: "))
fib_series = fibonacci(n)
print("Fibonacci series of the first", n, "numbers:")
print(fib_series)
