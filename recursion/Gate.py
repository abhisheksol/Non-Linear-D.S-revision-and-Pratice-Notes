def fun(n, p):
    if n <= 1:
        p[0] = 1
        return 1

    x = fun(n - 1, p)
    y = x + p[0]
    p[0] = x

    return y

def main():
    a = [15]
    print(fun(5, a))

if __name__ == "__main__":
    main()
