from time import time


class QuadratoMagico():

    def __init__(self,N):
        self.N = N
        self.n_chiamate = 0
        self.n_soluzioni = 0

    #soluzione del quadrato magico rappresentata da un vettore di N alla seconda elementi,
    #ogni elemento rappresenta una cella del quadrato e il suo valore è il numero che mettiamo nella cella
    def risolvi_quadrato(self):
        self.n_chiamate = 0
        self.n_soluzioni = 0
        self._ricorsione([])

    def _ricorsione(self, parziale):
        self.n_chiamate += 1
        if len(parziale) == self.N*self.N:
            self.n_soluzioni += 1
            print(parziale)
        else:
            for numero in range(1,self.N*self.N+1):
                #aggiungere numero a parziale
                parziale.append(numero)
                #andare avanti nella ricorsione
                self._ricorsione(parziale)
                #backtracking
                parziale.pop()

if __name__ == "__main__":
    qm = QuadratoMagico(2)
    start = time()
    qm.risolvi_quadrato()
    end = time()

    print(f"Tempo : {end-start}")
    print(f"Chiamate effettuate : {qm.n_chiamate}")
    print(f"Soluzione effettuate : {qm.n_soluzioni}")

# Riprendere da 40:00