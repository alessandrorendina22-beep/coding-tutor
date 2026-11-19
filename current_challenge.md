# Sfida del Giorno: Il Sistema Sconti della Bottega (Condizioni Multiple con `else if` e `&&`)

Finora hai gestito scelte binarie: *o compri, o non hai abbastanza monete* (`if ... else`). 

Nel mondo reale (e nei videogiochi!), però, le decisioni sono spesso a più livelli. Il nostro alchimista ha deciso di premiare i clienti più fedeli introducendo un **sistema di sconti a scaglioni** basato sulla quantità di pozioni acquistate!

Per gestire più di due alternative in C abbiamo due nuovi potenti alleati:
1. **`else if`**: serve per controllare una seconda (o terza, quarta...) condizione se la prima è risultata falsa:
   ```c
   if (livello >= 20) {
       printf("Sei un Veterano!\n");
   } else if (livello >= 10) {
       printf("Sei un Avventuriero!\n");
   } else {
       printf("Sei un Novizio!\n");
   }
   ```
2. **L'operatore logico `&&` (AND / "E contemporaneamente")**: permette di verificare che due condizioni siano vere nello stesso momento:
   ```c
   if (punti >= 50 && punti <= 100) {
       // Si attiva solo se i punti sono tra 50 e 100 compresi
   }
   ```

---

## Obiettivi

Crea un programma in C che calcoli il conto per l'acquisto delle pozioni applicando lo sconto corretto in base alla quantità acquistata:

1. **Richiesta dati (Input):**
   - Chiedi all'utente il prezzo di una singola pozione (decimale, `float`).
   - Chiedi quante pozioni vuole comprare (intero, `int`).

2. **Calcolo e Regole dello Sconto:**
   - Calcola il totale parziale (senza sconto).
   - Verifica lo sconto da applicare usando `if`, `else if` ed `else`:
     - **Scaglione 1:** Se compra **10 o più pozioni**, ha diritto al **20% di sconto**.
     - **Scaglione 2:** Se compra **tra 5 e 9 pozioni** (estremi compresi, usa l'operatore `&&`), ha diritto al **10% di sconto**.
     - **Scaglione 3:** Se compra **meno di 5 pozioni**, non c'è alcuno sconto (0%).

   *(Suggerimento matematico: per calcolare il 20% di sconto puoi fare `sconto = totale_parziale * 0.20;` e poi sottrarlo dal totale).*

3. **Stampa del scontrino (Output):**
   - Comunica quale percentuale di sconto è stata applicata (o se non è stato applicato alcuno sconto).
   - Stampa il prezzo totale finale da pagare, formattato con due cifre decimali (`%.2f`).

---

## La mia soluzione e i miei dubbi

```c
#include <stdio.h>

int main(){
    float costo_pozione, totale, totale_parziale, sconto;
    int numero_pozioni;

    printf("Inserisci il prezzo della singola pozione: ");
    scanf("%f", &costo_pozione);
    printf("Insersci il numero di pozioni: ");
    scanf("%d", &numero_pozioni);
    totale_parziale = numero_pozioni * costo_pozione;

    if (numero_pozioni >= 10){
        sconto = totale_parziale * 0.20;
        printf("è stato applicato lo sconto del 20%\n");
    }
    else if (numero_pozioni >=5 && numero_pozioni <=9){
        sconto = totale_parziale * 0.10;
        printf("è stato applicato lo sconto del 10%\n");
    }
    else{
        sconto = 0;
        printf("Non è stato applicato nessuno sconto.\n");
    }
    totale = totale_parziale - sconto;
    printf("Il totale con lo sconto è di %.2f monete", totale);
    return 0;
}
```

*non ho dubbi, ma ti sei dimenticato in questo prompt di mettere alla fine la sezione per inseire il codice. Non dimenticarlo piu. Per il resto è tutto ben fatto!*

---
# Correzione del Tutor
Ciao! Prima di tutto, grazie per la segnalazione: farò in modo di inserire sempre il template pronto per il codice nei prossimi esercizi! 😉

Passiamo ora all'analisi del tuo codice.

---

### Analisi del Codice

Il tuo programma è **eccellente**: pulito, perfettamente funzionante e rispetta alla lettera tutti i requisiti della traccia.

Ecco i punti di forza della tua soluzione:
1. **Scelta dei tipi corretta:** Hai usato `float` per i valori monetari e `int` per il conteggio delle pozioni, operando correttamente con le conversioni implicite nella moltiplicazione `totale_parziale = numero_pozioni * costo_pozione;`.
2. **Logica condizionale precisa:** Hai utilizzato `if`, `else if` ed `else` in maniera impeccabile, applicando esattamente l'operatore `&&` come richiesto.
3. **Formattazione dell'output:** Hai usato correttamente la specifica `%.2f` per mostrare due decimali sul prezzo finale.

---

### Piccoli spunti di miglioramento (Consigli da Pro)

Non ci sono veri e propri errori bloccanti, ma un paio di dettagli possono rendere il tuo codice ancora più professionale:

1. **Ridondanza logica (approfondimento teorico):**
   Hai scritto:
   ```c
   if (numero_pozioni >= 10) {
       ...
   } else if (numero_pozioni >= 5 && numero_pozioni <= 9) {
       ...
   }
   ```
   Poiché la traccia chiedeva espressamente di sperimentare l'operatore `&&`, **hai fatto benissimo a usarlo**. 
   Tuttavia, tieni a mente che in una catena `if - else if`, se il programma arriva all'istruzione `else if`, significa che la prima condizione (`>= 10`) era già **falsa**. Di conseguenza, il fatto che `numero_pozioni` sia minore o uguale a 9 è già matematicamente certo. In un contesto reale, sarebbe bastato scrivere `else if (numero_pozioni >= 5)`.

2. **Caratteri accentati nella console:**
   Hai scritto `printf("è stato applicato...");`. In ambiente Windows/DOS o a seconda dell'encoding del terminale, le lettere accentate dirette (come `è` o `à`) possono talvolta apparire con simboli strani (es. `Š` o caratteri ASCII non voluti). Per evitarlo, puoi scrivere `E' stato...` oppure configurare l'encoding del terminale su UTF-8.

3. **`\n` finale e refuso nel testo:**
   - Nel prompt hai scritto `"Insersci"` (manca una 'i').
   - Nell'ultimo `printf`, è buona norma chiudere con un a capo `\n`:
     ```c
     printf("Il totale con lo sconto è di %.2f monete\n", totale);
     ```

---

## Valutazione per il Tutor

**PROMOSSO: pronto per il livello successivo.**

Lo studente ha dimostrato piena comprensione della struttura `if - else if - else` e dell'operatore logico AND (`&&`). Il codice compila senza problemi, la gestione dei tipi di dato è corretta e lo stile di scrittura è pulito e leggibile. Nessuna criticità riscontrata.