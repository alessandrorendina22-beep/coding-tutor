# Sfida del Giorno: L'Allenamento del Guerriero (Il Ciclo `while`)

Finora i tuoi programmi hanno eseguito le istruzioni dall'alto verso il basso una sola volta, prendendo bivi grazie a `if` ed `else`. Ma cosa succede se dobbiamo ripetere la stessa azione decine, centinaia o migliaia di volte?

Nei videogiochi o nei software reali non scriviamo mille volte `printf`: usiamo i **cicli** (in inglese *loops*).

Oggi esploriamo il ciclo più intuitivo: il ciclo **`while`** (che in italiano significa *"mentre"* o *"finché"*).

### Come funziona il `while`?
La sintassi è molto simile a un `if`:
```c
while (condizione) {
    // Codice che viene ripetuto FINCHÉ la condizione è vera
}
```
Il computer controlla la condizione: se è vera, esegue il blocco tra parentesi graffe `{}`. Quando arriva in fondo, torna su a controllare di nuovo la condizione. Continua a ripetere finché la condizione non diventa **falsa**.

> ⚠️ **Attenzione al Loop Infinito:** Ricordati sempre di modificare la variabile di controllo dentro il ciclo (ad esempio aumentandola con `contatore = contatore + 1;` o la sua scorciatoia `contatore++;`), altrimenti il ciclo non si fermerà mai!

---

### La Missione
Il guerriero Kevin deve prepararsi alla prossima avventura e si allena colpendolo un manichino da combattimento.

Chiedi all'utente quanti colpi Kevin deve sferrare. Dopodiché, usa un ciclo `while` per simulare l'allenamento, stampando ogni singolo fendente fino a raggiungere il totale richiesto!

---

## Obiettivi

1. **Dichiarare le variabili necessarie:** 
   - Una variabile intera per i colpi totali scelti dall'utente.
   - Una variabile "contatore" (es. `int colpo = 1;`) per tenere traccia del colpo corrente.
2. **Input utente:** Chiedi all'utente quanti colpi vuole far fare a Kevin usando `printf` e `scanf`.
3. **Il Ciclo `while`:** 
   - Finché il `colpo` corrente è minore o uguale al totale richiesto:
     - Stampa a video il numero del colpo sferrato (es. `Fendente numero 1 sferrato!`).
     - Incrementa il contatore di 1 (`colpo++;`).
4. **Fine allenamento:** Una volta terminato il ciclo, stampa un messaggio conclusivo che celebri la fine dell'allenamento.

#### Esempio di esecuzione:
```text
Quanti colpi di allenamento deve sferrare Kevin? 3

--- Inizio Allenamento ---
Fendente numero 1 sferrato!
Fendente numero 2 sferrato!
Fendente numero 3 sferrato!
--- Allenamento completato! Kevin e' piu' forte di prima! ---
```

---

## La mia soluzione e i miei dubbi

```c
#include <stdio.h>

int main(){
    int i, colpo = 1;
    printf("Quanti colpi vuoi che sferri Kevin? ");
    scanf("%d", &i);
    while(colpo <= i){
        printf("Fendente numero %d sferrato!\n",colpo);
        colpo++;
    }
    printf("\"Allenamento completato! Kevin e' piu' forte di prima!\"\n");
    return 0;
}

```

*Tutto chiaro!*

---
# Correzione del Tutor
Ciao! Ottimo lavoro, hai completato la sfida in modo impeccabile!

Ecco un'analisi dettagliata del tuo codice e qualche piccolo consiglio per migliorare ulteriormente.

---

### Analisi del Codice

1. **Logica del ciclo `while`:** 
   Hai impostato perfettamente la condizione `colpo <= i`. Partendo da `colpo = 1`, il ciclo esegue esattamente il numero di iterazioni richieste dall'utente.
2. **Incremento del contatore:** 
   L'istruzione `colpo++;` è posizionata correttamente all'interno del blocco. In questo modo si evita il rischio di creare un ciclo infinito.
3. **Formattazione e output:** 
   L'uso dei caratteri di escape per le virgolette (`\"...\"`) nella riga finale è un ottimo tocco di stile che dimostra una buona padronanza della sintassi di base.

---

### Piccoli consigli da "Pro" (Best Practices)

Il tuo codice funziona al 100%, ma ecco due dettagli che possono renderlo ancora più professionale:

1. **Convenzione sui nomi delle variabili:**
   * Di solito, nei linguaggi di programmazione, lettere brevi come `i`, `j`, `k` si usano per i **contatori** (gli indici).
   * Per la variabile che memorizza il valore scelto dall'utente sarebbe preferibile un nome descrittivo come `colpi_totali` o `numero_colpi`.
   * Nel tuo caso hai usato `colpo` per il contatore (ottimo nome!) e `i` per il limite massimo: invertirli o usare `totale_colpi` renderebbe il codice ancora più chiaro a colpo d'occhio.

2. **Cosa succede con numeri minori di 1?**
   * Se l'utente inserisce `0` o `-5`, la condizione `colpo <= i` (`1 <= 0`) risulterà subito falsa: il ciclo verrà saltato e Kevin completerà l'allenamento senza dare fendenti. 
   * Il ciclo `while` gestisce questa casistica in modo naturale (controlla la condizione *prima* di eseguire il corpo), il che è corretto! Più avanti vedremo come validare l'input dell'utente con controlli dedicati.

---

## Valutazione per il Tutor

**PROMOSSO: pronto per il livello successivo**

Lo studente ha compreso appieno il funzionamento del ciclo `while`, la corretta inizializzazione del contatore, la condizione di terminazione e l'incremento. Ha svolto la consegna in autonomia senza dubbi residui. Si può procedere con i prossimi argomenti (es. ciclo `for` o `do-while`).