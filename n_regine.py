import copy
from time import time
class NRegine():
    def __init__(self):
        self.n_soluzioni=0 #voglio contare quante soluzioni ci sono
        self.n_chiamate=0
        self.soluzioni=[] #in questa lista voglio salvarmi le soluzioni per poter confrontare se una delle nuove non è già presente, ma magari in ordine diverso
        #come se avessi sol1 [[3,1],[2,2]...] e poi sol2 [[2,2],[3,1]...] --> non lo implementiamo adesso

    def solve(self,N):
        """metodo in cui faccio partire la ricorsione"""
        self.n_soluzioni=0 #lo devo reimpostare a 0
        self.n_chiamate=0
        self._ricorsione([],N)




    def _ricorsione(self,parziale,N):
        """metodo ricorsivo che faccio girare piu volte. parziale è una lista in cui metto dentro delle coppie"""
        self.n_chiamate+=1 #voglio vedere quante volte viene chiamato il metodo ricorsione

        #condizione terminale: quando parziale ha lunghezza N --> ho raggiunto una possibile soluzione (non ho ancora controllato se la regine sono in posizioni in cui non si mangiano)
        if len(parziale) == N :
            #provo a controllare i vincoli nell'if
           # if self.is_soluzione(parziale): --> questo check non mi serve piu perchè ho gia controllato nella funzione ricorsiva
                print(parziale)
                self.soluzioni.append(copy.deepcopy(parziale))
                self.n_soluzioni+=1
        #caso ricorsivo:
        else:
            for riga in range(N):
                for col in range(N):
                    #provo nuova ipotesi, ma voglio controllare subito se la nuova regina che considero verrebbe , mangiata o no:
                    nuova_regina=[riga,col]
                    if self.is_valid(nuova_regina, parziale):
                        parziale.append([riga,col])
                        #vado avanti nella ricorsione:
                        self._ricorsione(parziale,N)
                        # backtracking:
                        parziale.pop() #qua torna inidetro fino alla root dell'albero e esplora un nuovo percorso


#vincoli da implementare : ho già una regina nella lista, devo aggiungerne un'altra che non può essere mangiata dalla prima
#la nuova regina non deve essere nè nella stassa riga nè nella stessa colonna ma neanche nelle 2 diagonali (4 vincoli PER OGNI REGINA presente nella scacchiera)
#vincolo di riga --> conosciamo la riga della regina già presente, la nuova riga deve essere diversa dalla riga già occupata
#vincolo di colonna --> analogo a vincolo di riga
#vincolo prima diagonale (che va in senso crescente --> da in basso a sx a in alto a dx) --> la somma degi indici di riga + colonna è costante, quindi la nuova regina deve essere in posizioni tali per cui la somma degli indici di riga e colonna non è uguale a quella della regina già presente
#vincolo seconda diagonale (che va da top right a bottom left) --> la DIFFERENZA degli indici riga - colonna è costante
#questi controlli vanno fatti rispetto a tutte le regine già inserite

    def is_admissible(self, regina1, regina2):
        """IMPLEMENTAZIONE DEI VINCOLI :funzione che controlla se DUE regine si mangiano fra di loro"""
        #verifico riga, se non va bene return False:
        if regina1[0]==regina2[0]:
            return False
        #verifico colonna:
        if regina1[1]==regina2[1]:
            return False
        #verifico diagonale crescente:
        if (regina1[0]+regina1[1])==(regina2[0]+regina2[1]):
            return False
        #verifico diagonale decrescente:
        if (regina1[0]-regina1[1])==(regina2[0]-regina2[1]):
            return False
        #ho passato tutti i controlli, return True:
        return True

    def is_soluzione(self, parziale):
        """funzione in cui controllo se TUTTE le regine della lista parziale non si mangiano tra di loro --> chiamo funzione is_admissible a due a due"""
        for i in range(len(parziale)-1):
            for j in range(i+1,len(parziale)): #devo mettere i range in questo modo perchè se no confornta una regina con se stessa ed esce subito False
                result=self.is_admissible(parziale[i],parziale[j])
                if result==False:
                    return False #mi basta che solo una volta non vada bene una regina ed esco
        return True #se non ho mai trovato un caso false, ritorno True

    def is_valid(self, nuova_regina, parziale):
        """funzione che controlla se la regina nuova che considero, va bene con le regine che ho già nella soluzione parziale"""
        for regina in parziale:
            if not self.is_admissible(nuova_regina, regina):
                return False
        return True


#il controllo dei vincoli può essere fatto in vari punti:
#1) nell'if, dopo aver riempito la lista, controllo se quelle che ho messo vanno bene --> non va bene perchè comunque ho lavorato un sacco per niente
#2) prima di aggiungere una nuova regine nell'else --> più efficace



if __name__ == '__main__':
    nreg=NRegine()
    start_time = time()
    nreg.solve(4)
    end_time = time()
    print(f"Elapsed time: {end_time - start_time}")
    print(f"Numero (possibili) soluzioni= {nreg.n_soluzioni}")
    print(f"Numero chiamate= {nreg.n_chiamate}")
