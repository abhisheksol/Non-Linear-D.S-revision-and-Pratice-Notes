def fib(n):
    if n == 1:
        return 1
    elif n==0:
        return 0
    data= fib(n -2) + fib(n - 1)
    # print(data)
    return data

print(fib(7))
