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
*(Scrivi qui il tuo codice C e qualsiasi dubbio o domanda ti sia venuta durante la scrittura!)*
```c

```