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