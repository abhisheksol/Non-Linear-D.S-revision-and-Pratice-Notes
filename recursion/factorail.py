# 5 4 3 2 1
# store=1
# n=5
# for i in range(1,n+1):
#     store*=i

# print(store)

def fact(n):
    if n <= 1:
        return 1
    store = n * fact(n - 1)
    #       5*4*3*2
    print(store)
    return store

fact(5)
