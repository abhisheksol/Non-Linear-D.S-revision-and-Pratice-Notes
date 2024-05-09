def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)

print(fib(5))

# def fib_series(n):
#     fib_list = [0, 1]
    
#     for i in range(2, n):
#         fib_list.append(fib_list[-1] + fib_list[-2])

#     return fib_list

# n = 5
# result = fib_series(n)
# print(result)
