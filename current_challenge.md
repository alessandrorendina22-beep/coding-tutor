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