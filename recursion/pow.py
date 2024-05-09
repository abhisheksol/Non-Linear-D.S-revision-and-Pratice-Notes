def pow(x,n):
    if n==0:
        return 1
    data=pow(x,n-1)
    return x*data

print(pow(2,3))