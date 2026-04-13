def binomial(n, m):
    pass

def binomial_recursive(n, m):
    if n>=0 and n >= m >= 0:
        if m == n or m == 0:
            return 1
        else:
            return binomial_recursive(n - 1, m) + binomial_recursive(n - 1, m - 1)
    else:
        return "Not possible"

if __name__ == '__main__':
    n = 5
    m = 3
    print(binomial_recursive(n, m))