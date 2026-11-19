# Sfida del Giorno: La Bottega Interattiva (Input con `scanf`)

Fino ad ora i tuoi programmi erano "statici": i valori delle pozioni e dei prezzi erano scritti direttamente nel codice sorgente. Se un cliente voleva comprare 5 pozioni invece di 3, toccava a te modificare il codice e ricompilarlo ogni volta!

Oggi facciamo fare un vero salto di qualità ai tuoi programmi rendendoli **interattivi**: impareremo a chiedere i dati direttamente a chi usa il programma tramite la tastiera.

Per farlo useremo la funzione gemella di `printf`: **`scanf`** (che sta per *scan formatted*).

---

### Breve guida rapida: come funziona `scanf`?
Funziona in modo molto simile a `printf`, con una piccola ma fondamentale differenza: dobbiamo usare il simbolo **`&`** (la e commerciale o "ampersand") prima del nome della variabile.

```c
int quantita;
printf("Quanti oggetti vuoi comprare? ");
scanf("%d", &quantita); // Nota il & davanti a quantita!
```
> **Perché serve la `&`?**  
> Pensa alle variabili come a delle scatole con un'etichetta. Con `scanf`, dobbiamo indicare al computer l'**indirizzo** della scatola dove andare a riporre il dato inserito dall'utente. Il simbolo `&` serve proprio a dire: *"Metti il valore preso da tastiera all'indirizzo di memoria di questa variabile"*.

Per i numeri con la virgola (`float`) la logica è identica:
```c
float prezzo;
printf("Inserisci il prezzo: ");
scanf("%f", &prezzo);
```

---

## Obiettivi

Scrivi un programma in C che simuli la cassa interattiva di un negozio per avventurieri:

1. **Dichiarare le variabili necessarie:** ti servirà un intero per la quantità di pozioni, un decimale (`float`) per il costo unitario e un decimale per il totale.
2. **Chiedere i dati all'utente:**
   - Mostra un messaggio a video che chieda all'utente quante pozioni vuole acquistare e salva il dato con `scanf`.
   - Mostra un messaggio che chieda all'utente il prezzo di una singola pozione e salva il dato con `scanf`.
3. **Calcolare il totale:** calcola l'importo complessivo moltiplicando la quantità per il prezzo unitario.
4. **Stampare lo scontrino finale:**
   - Mostra un riepilogo con: quantità acquistata, prezzo singolo (con 2 decimali) e costo totale (con 2 decimali).
   - Includi una frase di ringraziamento racchiusa tra virgolette (`\"`).
5. **Buone pratiche:** ricordati di includere `return 0;` alla fine del `main` e di curare la leggibilità degli spazi.

---

## La mia soluzione e i miei dubbi

```c
#include <stdio.h>

int main(){
    int quantita_pozioni;
    float costo_unitario, totale;
    printf("Quante pozioni vuoi acquistare?\n");
    scanf("%d",&quantita_pozioni);
    printf("Inserisci il prezzo di una singola pozione: \n");
    scanf("%f",&costo_unitario);
    totale=costo_unitario*quantita_pozioni;
    printf("Il numero di pozioni acquistate è %d\n",quantita_pozioni);
    printf("Il costo singolo di una pozione è %.2f\n",costo_unitario);
    printf("Il totale ammonta a %.2f\n",totale);
    printf("\"Grazie e buona giornata\"");
    return 0;
}


```

*Tutto chiaro!*