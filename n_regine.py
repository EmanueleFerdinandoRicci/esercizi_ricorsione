import copy
from contextlib import nullcontext
from time import time

class Regina():
    def __init__(self,riga,colonna):
        self.riga = riga
        self.colonna = colonna

class NRegine():

    def __init__(self):
        self.n_soluzioni = 0
        self.n_chiamate = 0
        self.soluzioni = []
        self.soluzioni_uniche = set()

    #====================APPROCCIO 2============================
    #rappresentiamo soluzione come un vettore di N regine,
    #ognuno rappresentante una regina come riga e colonna
    def solve_coordinate(self,N):
        self.n_soluzioni = 0
        self.n_chiamate = 0
        self.soluzioni = []
        self.soluzioni_uniche = set() #con un set però serve usare la classe Regina
        self._ricorsione_coordinate([],N)

    #parziale è un vettore di coppie (coordinate riga-colonna)
    def _ricorsione_coordinate(self,parziale,N):
        self.n_chiamate += 1
        #caso terminale: ho messo N regine
        if len(parziale) == N:
            #if self._is_soluzione(parziale): diventa in questo momento ricorsivo per verifica già fatta precedentemente
            #    self.n_soluzioni += 1
            #    print(parziale)
            if self._is_nuova_soluzione(parziale):
                self.n_soluzioni += 1
                self.soluzioni.append(copy.deepcopy(parziale))
            #print(parziale)
        #caso ricorsivo: ho messo meno di N regine
        else:
            for riga in range(N):
                for col in range(N):
                    nuova_regina = [riga,col]
                    #verifico se ammissibile
                    if self._step_is_valid(nuova_regina,parziale):
                        #aggiungo la regina alla soluzione
                        parziale.append(nuova_regina)
                        #continuo ricorsione
                        self._ricorsione_coordinate(parziale,N)
                        #backtracking, per provare tutte le possibili soluzioni
                        parziale.pop()

    # funzione per capire se la soluzione non è stata già ancora trovata
    def _is_nuova_soluzione(self,soluzione_potenziale):
        N = len(soluzione_potenziale)
        for soluzione in self.soluzioni:
            counter = 0
            for regina in soluzione_potenziale:
                if regina in soluzione:
                     counter += 1
            if counter == N:
                return False
        return True

    # funzione che controlla se la nuova regina da inserire sia ammissibile rispetto alla soluzione parziale
    def _step_is_valid(self,nuova_regina,parziale) -> bool :
        for regina in parziale:
            if not self._is_pair_admissible(nuova_regina,regina):
                return False
        return True

    # funzione che prende due regine e restituisce True se non si possono attaccare
    # altrimenti True
    def _is_pair_admissible(self, regina1, regina2) ->bool:
        # 1 verifica sulla riga
        if regina1[0] == regina2[0]:
            return False
        # 2 verifica sulla colonna
        if regina1[1] == regina2[1]:
            return False
        # 3 verifia di una diagonale
        # per una diagonale da sx in alto a dx in basso si ha che la differenza riga - colonna è costante
        # quindi non accettabile se riga reg1 - col reg1 == riga reg2 - col reg2
        if regina1[0] - regina1[1] == regina2[0] - regina2[1]:
            return False
        # 4 verifica dell'altra diagonale
        # per una diagonale da sx in basso a dx in alto la somma colonna + riga è costante
        # non accettabile se col reg1 + riga reg1 == col reg2 + riga reg2
        if regina1[0] + regina1[1] == regina2[0] + regina2[1]:
            return False
        # 5 ho passato tutti i controlli, return True
        return True

    # metodo che data possibile soluzione (lista con N regine) verifica se sia ammissibile
    def _is_soluzione(self, soluzione_possibile) -> bool:
        for i in range(len(soluzione_possibile)):
            for j in range(i+1,len(soluzione_possibile)):
                if not self._is_pair_admissible(soluzione_possibile[i],soluzione_possibile[j]):
                    return False
        return True


if __name__ == "__main__":
    nreg = NRegine()
    start_time = time()
    nreg.solve_coordinate(4)
    end_time = time()

    print(f"Tempo operazione: {end_time - start_time}")
    print(f"Ho trovato {nreg.n_soluzioni} soluzioni possibili")
    print(f"Chiamate effettuate: {nreg.n_chiamate}")
    print(nreg.soluzioni)