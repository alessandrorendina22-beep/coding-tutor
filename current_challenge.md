# Sfida del Giorno: La Cassa della Bottega (Le Decisioni con `if` ed `else`)

Fino ad ora i tuoi programmi hanno eseguito istruzioni in linea retta, dall'alto verso il basso: chiedi dei dati, fai un calcolo e stampi il risultato. 

Nel mondo reale (e nei videogiochi!), però, i programmi devono saper **prendere decisioni**. Ad esempio: *il cliente ha abbastanza soldi nel portafoglio per pagare?*

In C, per prendere decisioni utilizziamo il costrutto condizionale **`if` ... `else`** accompagnato dagli operatori di confronto (come `>`, `<`, `>=`, `==` per verificare l'uguaglianza).

Ecco la sintassi di base:
```c
if (condizione) {
    // codice eseguito solo se la condizione è VERA
} else {
    // codice eseguito se la condizione è FALSA
}
```

Torniamo alla nostra amata **Bottega dell'Alchimista**! Questa volta vogliamo rendere la cassa intelligente: controlleremo se il cliente ha abbastanza monete d'oro per completare l'acquisto o se deve tornare a fare qualche missione per racimolare denaro.

---

## Obiettivi

Scrivi un programma in C che:
1. Chieda all'utente:
   - Il prezzo di una singola pozione (`float`).
   - La quantità di pozioni da acquistare (`int`).
   - Quante monete d'oro ha a disposizione nel borsello (`float`).
2. Calcoli il **costo totale** dell'acquisto.
3. Usi un blocco **`if` / `else`** per verificare se il denaro a disposizione è sufficiente:
   - **Se il denaro è sufficiente (o pari al totale):** stampa un messaggio di successo, mostra il resto che gli rimane (denaro a disposizione - costo totale) formattato a 2 cifre decimali (`%.2f`) e un saluto amichevole.
   - **Se il denaro NON è sufficiente:** stampa un messaggio di avviso dicendo chiaramente quante monete mancano all'appello per poter comprare le pozioni.

---

## La mia soluzione e i miei dubbi
*Vorrei capire se è meglio dichiarare piu variabili o utilizzarne una con 2 differenti utilizzi come la variabile resto in questo caso.*
```c
#include <stdio.h>

int main(){
    int quantita_pozioni;
    float costo_unitario, totale, monete, resto;

    printf("Inserisci il prezzo di una singola pozione: ");
    scanf("%f", &costo_unitario);
    printf("Quante pozioni vuoi acquistare? Inserisci il numero: ");
    scanf("%d", &quantita_pozioni);
    totale=costo_unitario*quantita_pozioni;
    printf("Quante monete hai a disposizione? Inserisci il numero: ");
    scanf("%f", &monete);
    if (monete>=totale){
        printf("Perfetto! Monete sufficienti. \n");
        resto=monete-totale;
        printf("Il resto rimanente è %.2f monete\n",resto);
    }
    else{
        printf("Monete non sufficienti!");
        resto=totale-monete;
        printf("Ti mancano %.2f monete",resto);
    }
    return 0;
}

```