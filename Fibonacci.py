from functools import lru_cache
from time import time

class Fibonacci:
    def __init__(self):
        self.cache = {0:0,1:1}

    def calcola_elemento_cache(self,n):
        #se ho già soluzione la prendo dalla cache
        if self.cache.get(n) is not None:
            return self.cache[n]
        #sennò ricorsivo
        else:
            self.cache[n] = (self.calcola_elemento_cache(n-1) + self.calcola_elemento(n-2))
            return self.cache[n]

    @lru_cache
    def calcola_elemento_lru(self,n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            self.cache[n] = (self.calcola_elemento_lru(n-1) + self.calcola_elemento_lru(n-2))
            return self.cache[n]

    def calcola_elemento(self,n):
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            return self.calcola_elemento(n-1) + self.calcola_elemento(n-2)

if __name__ == "__main__":
    N=20
    fib = Fibonacci()

    start = time()
    print(fib.calcola_elemento(N))
    end = time()
    print(f"Tempo di esecuzione : {end-start}")

    start = time()
    print(fib.calcola_elemento_cache(N))
    end = time()
    print(f"Tempo di esecuzione : {end - start}")

    start = time()
    print(fib.calcola_elemento_lru(N))
    end = time()
    print(f"Tempo di esecuzione : {end - start}")