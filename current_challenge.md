# Sfida del Giorno

### Livello 2: La Bottega dell'Alchimista (Introduzione alle Variabili)

Complimenti per aver superato il primo livello! Finora hai stampato a schermo solo testi "fissi". Nel mondo reale, però, i programmi devono memorizzare informazioni che possono cambiare: punti vita, monete d'oro, punteggi, ecc. Per farlo, usiamo le **variabili**!

Pensa a una variabile come a una **scatola con un'etichetta** in cui puoi inserire un valore. In C dobbiamo sempre dire al computer di che tipo è la scatola:
- `int`: per numeri **interi** (es. `3`, `42`, `-5`).
- `float`: per numeri con la **virgola** (es. `9.99`, `1.75`). *(Nota: in programmazione si usa il punto al posto della virgola!)*

Per stampare il contenuto di queste "scatole" con `printf`, usiamo dei segnaposto chiamati **specificatori di formato**:
- `%d` per gli interi (`int`)
- `%f` per i decimali (`float`) — se scrivi `%.2f`, il computer mostrerà solo due cifre decimali dopo il punto, perfetto per i prezzi!

Ecco un piccolo esempio:
```c
int monete = 50;
float peso = 12.5;

printf("Hai %d monete d'oro.\n", monete);
printf("Il tuo zaino pesa %.2f kg.\n", peso);
```

Inoltre, puoi fare calcoli direttamente nel codice usando gli operatori matematici base: `+`, `-`, `*` (moltiplicazione), `/` (divisione).

---

## Obiettivi

Immagina di essere il cassiere della Bottega dell'Alchimista. Un guerriero entra per fare rifornimento prima della battaglia. Scrivi un programma in C che:

1. Crei una variabile intera (`int`) per il **numero di pozioni** acquistate (scegli tu quante, ad esempio `3`).
2. Crei una variabile decimale (`float`) per il **prezzo singolo** di una pozione (ad esempio `4.50`).
3. Calcoli la spesa totale moltiplicando il numero di pozioni per il prezzo singolo e salvi il risultato in una nuova variabile decimale (`float totale = ...`).
4. Stampi uno scontrino chiaro e ben formattato a video che mostri:
   - Il numero di pozioni comprate (usando `%d`).
   - Il costo di una singola pozione (usando `%.2f`).
   - Il totale da pagare (usando `%.2f`).
   - Un messaggio di saluto finale tra virgolette (sfruttando il trucco di `\"` che abbiamo visto!).

---

## La mia soluzione e i miei dubbi

```c
#include <stdio.h>

int main(){
    int pozioni=3;
    float prezzo_singolo=2.50;
    float totale=pozioni*prezzo_singolo;
    printf("Il numero delle pozioni comprate è %d\n", pozioni);
    printf("Il costo della singola pozione è %.2f\n", prezzo_singolo);
    printf("Il totale da pagare è %.2f\n", totale);
    printf("\"Buona giornata e grazie di essere passati qui alla Bottega dell'Alchimista\"\n");
}


```

*Argomento molto interessante sopratutto gli specificatori di formato*

---
# Correzione del Tutor
Ciao! È un piacere vedere il tuo entusiasmo per gli specificatori di formato: sono davvero uno degli strumenti fondamentali del C per comunicare con l'utente in modo ordinato e professionale.

Vediamo insieme l'analisi del tuo codice!

---

### Analisi della Soluzione

Il tuo codice è **eccellente**. Hai centrato in pieno tutti gli obiettivi richiesti dalla consegna. Ecco cosa hai fatto particolarmente bene:

1. **Scelta e inizializzazione delle variabili:**
   - Hai usato correttamente `int` per `pozioni` e `float` per `prezzo_singolo`.
   - Il calcolo `float totale = pozioni * prezzo_singolo;` è perfetto. Il C effettua in automatico una *conversione implicita* (promuove l'intero a float durante l'operazione) per garantirti un risultato decimale preciso.
2. **Specificatori di formato:**
   - Hai usato `%d` per l'intero e `%.2f` per i decimali. Il formato `%.2f` è la scelta ideale per gestire valori monetari o misure che richiedono solo due cifre decimali.
3. **Sequenze di escape:**
   - Ottimo l'uso di `\"` per stampare le virgolette senza interrompere la stringa e di `\n` per andare a capo.

---

### Piccoli consigli da professionista (Best Practices)

Non ci sono veri e propri errori nel tuo codice, ma ecco due dettagli per renderlo ancora più solido:

1. **Aggiungere `return 0;` alla fine del `main`:**
   In C, la funzione `main` restituisce un intero (`int main()`). Scrivere `return 0;` prima della parentesi graffa di chiusura è una buona abitudine: comunica al sistema operativo che il programma è terminato con successo (senza errori).
   ```c
       printf("\"Buona giornata e grazie di essere passati qui alla Bottega dell'Alchimista\"\n");
       return 0;
   }
   ```
2. **Spaziature per la leggibilità (Stile):**
   Mettere uno spazio attorno agli operatori rende il codice più facile da leggere:
   - Scrivi `int pozioni = 3;` invece di `int pozioni=3;`
   - Scrivi `float totale = pozioni * prezzo_singolo;`

---

## Valutazione per il Tutor

**PROMOSSO: pronto per il livello successivo.**  
Lo studente ha compreso pienamente l'uso dei tipi `int` e `float`, le operazioni aritmetiche di base, la formattazione dell'output con `printf` (`%d`, `%.2f`) e le sequenze di escape (`\"`, `\n`). Nessun errore concettuale riscontrato.