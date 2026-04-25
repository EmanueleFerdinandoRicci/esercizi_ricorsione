import copy
from time import time


class QuadratoMagico():

    def __init__(self,N):
        self.N = N
        self.n_chiamate = 0
        self.n_soluzioni = 0
        self.soluzioni = []

    #soluzione del quadrato magico rappresentata da un vettore di N alla seconda elementi,
    #ogni elemento rappresenta una cella del quadrato e il suo valore è il numero che mettiamo nella cella
    def risolvi_quadrato(self):
        self.n_chiamate = 0
        self.n_soluzioni = 0
        self.soluzioni = []
        self._ricorsione([], set(range(1,self.N*self.N+1)))

    def _ricorsione(self, parziale, rimanenti):
        self.n_chiamate += 1
        if len(parziale) == self.N*self.N:
            if self._is_valid(parziale):
                self.n_soluzioni += 1
                self.soluzioni.append(copy.deepcopy(parziale))
                #print(parziale)
        else:
            for numero in rimanenti:
                #aggiungere controllo dei vincoli
                #aggiungere numero a parziale
                parziale.append(numero)
                # aggiungere controllo dei vincoli
                if self._is_parziale_valid(parziale):
                    #tolgo il numero inserito da rimanenti
                    nuovi_rimanenti = copy.deepcopy(rimanenti)
                    nuovi_rimanenti.remove(numero)
                    #andare avanti nella ricorsione
                    self._ricorsione(parziale,nuovi_rimanenti)
                #backtracking
                parziale.pop()

    def stampa_quadrato(self,soluzione):
        print("================")
        for riga in range(self.N):
            print(soluzione[riga*self.N:(riga+1)*self.N])
        print("================")

    def _is_valid(self, potenziale_soluzione):
        # controllo righe
        # controllo colonne
        # controllo diagonali
        # passati tutti True
        numero_magico = self.N*(self.N*self.N+1)/2
        for id_riga in range(self.N):
            riga = potenziale_soluzione[id_riga*self.N:(id_riga+1)*self.N]
            if sum(riga) != numero_magico:
                return False
        for id_col in range(self.N):
            col = potenziale_soluzione[id_col:(self.N-1)*self.N +id_col+1:self.N]
            if sum(col) != numero_magico:
                return False
        for id_diag1 in range(self.N):
            diag1 = potenziale_soluzione[0:self.N**2+1:self.N+1]
            if sum(diag1) != numero_magico:
                return False
        somma = 0
        for id_diag2 in range(self.N):
            somma += potenziale_soluzione[id_diag2*self.N+(self.N-1-id_diag2)]
        if somma != numero_magico:
            return False
        return True

    def _is_parziale_valid(self, parziale):
        # controllo righe
        # controllo colonne
        # controllo diagonali
        # passati tutti True
        numero_magico = self.N*(self.N*self.N+1)/2

        n_righe_completate = len(parziale)//self.N
        for id_riga in range(n_righe_completate):
            riga = parziale[id_riga*self.N:(id_riga+1)*self.N]
            if sum(riga) != numero_magico:
                return False
        n_col_completate = max(len(parziale)-self.N*(self.N-1),0)
        for id_col in range(n_col_completate):
            col = parziale[id_col:(self.N-1)*self.N +id_col+1:self.N]
            if sum(col) != numero_magico:
                return False
        #for id_diag1 in range(self.N):
        #    diag1 = potenziale_soluzione[0:self.N**2+1:self.N+1]
        #    if sum(diag1) != numero_magico:
        #        return False
        #somma = 0
        #for id_diag2 in range(self.N):
        #    somma += potenziale_soluzione[id_diag2*self.N+(self.N-1-id_diag2)]
        #if somma != numero_magico:
        #    return False
        return True


if __name__ == "__main__":
    qm = QuadratoMagico(3)
    start = time()
    qm.risolvi_quadrato()
    end = time()

    print(f"Tempo : {end-start}")
    print(f"Chiamate effettuate : {qm.n_chiamate}")
    print(f"Soluzione effettuate : {qm.n_soluzioni}")
    for soluzione in qm.soluzioni:
        qm.stampa_quadrato(soluzione)