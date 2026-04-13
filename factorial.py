def factorial(n):
    pass

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else :
        return n * factorial_recursive(n-1)


if __name__ == '__main__':
    N=4
    print(factorial_recursive(N))
