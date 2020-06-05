# Fibonacci till the value less than 100

def fib(n):
    a = 0
    b = 1

    if n < 0:
        print("Please enter positive number only")

    elif n == 1:
        print(a)

    else:
        print(a)
        print(b)
    for i in range(2, n):
        c = a + b
        a = b
        b = c
        if c > 100:
            break
        print(c)


fib(100)
