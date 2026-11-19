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

---
# Correzione del Tutor
Ciao! Ottimo lavoro: il programma **funziona correttamente** e rispetta alla perfezione tutti i requisiti della sfida. La logica della condizione `if (monete >= totale)` è impeccabile.

Vediamo insieme l'analisi del codice, la risposta al tuo dubbio e qualche consiglio per scrivere codice ancora più pulito.

---

### 1. Risposta alla tua domanda: Meglio riusare una variabile o dichiararne una nuova?

Hai posto una domanda eccellente che tocca un tema fondamentale della programmazione: la **leggibilità** vs il **riutilizzo delle risorse**.

> **Regola d'oro moderna:** È quasi sempre meglio **dare a ogni concetto una variabile con un nome chiaro** (oppure non usare affatto una variabile), piuttosto che riutilizzare la stessa variabile con significati diversi.

Ecco i motivi:
1. **Semantica e chiarezza:** La parola `resto` significa *denaro che torna indietro*. Nel blocco `else`, però, quel valore rappresenta il *denaro mancante*. Chiamarlo `resto` rende il codice meno intuitivo per chi lo legge (o per te stesso tra qualche mese).
2. **Uso della memoria:** Un tempo (negli anni '70/'80 o su sistemi embedded piccolissimi) risparmiare 4 byte di memoria per un `float` poteva fare la differenza. Oggi, nei computer moderni, la priorità assoluta è la **chiarezza e la manutenibilità del codice**.

#### Due alternative più pulite:

**Opzione A: Variabili separate con nomi chiari (anche dichiarate nei rispettivi blocchi)**
```c
if (monete >= totale) {
    float resto = monete - totale;
    printf("Il resto rimanente è %.2f monete\n", resto);
} else {
    float mancanti = totale - monete;
    printf("Ti mancano %.2f monete\n", mancanti);
}
```
*(Nota: dal C99 in poi puoi dichiarare le variabili direttamente all'interno delle parentesi graffe `{}` del blocco dove ti servono!)*

**Opzione B: Calcolo direttamente nel `printf` (senza variabili extra)**
Se il valore ti serve solo per essere stampato una volta sola, non sei obbligato a creare una variabile:
```c
if (monete >= totale) {
    printf("Il resto rimanente è %.2f monete\n", monete - totale);
} else {
    printf("Ti mancano %.2f monete\n", totale - monete);
}
```

---

### 2. Piccoli dettagli di stile e formattazione

1. **Aggiungi i caratteri di a capo (`\n`):**
   Nel ramo `else` hai dimenticato `\n`:
   ```c
   printf("Monete non sufficienti!\n"); // aggiunto \n per evitare che si attacchi alla riga successiva
   printf("Ti mancano %.2f monete\n", totale - monete);
   ```
2. **Spazi attorno agli operatori:**
   Invece di `totale=costo_unitario*quantita_pozioni;`, usa gli spazi:
   `totale = costo_unitario * quantita_pozioni;`
   Rende il codice molto più arioso e facile da leggere.

---

## Valutazione per il Tutor

**PROMOSSO: pronto per il livello successivo.**  
Lo studente ha compreso appieno il funzionamento del costrutto `if ... else` e la gestione delle condizioni logiche. Ha inoltre mostrato un ottimo spirito critico ponendo una domanda pertinente sulle buone pratiche di progettazione del codice. Può tranquillamente procedere con le condizioni composte (operatori logici `&&`, `||`, `!`) o con le strutture di controllo successive (`switch` o primi cicli).