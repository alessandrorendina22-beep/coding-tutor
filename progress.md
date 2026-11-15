

### Revisione recente
Ciao! Ottimo lavoro per essere il tuo primo programma in C. 

La struttura di base è impeccabile: hai incluso la libreria corretta (`<stdio.h>`), impostato la funzione `main`, usato `printf` con i caratteri di a capo (`\n`) e restituito correttamente `0`.

Ci sono però un paio di dettagli importanti e un piccolo "trucco del mestiere" che vale la pena approfondire!

---

### 1. Il dettaglio mancante: le virgolette (`\"`)
Nella consegna c'era una richiesta specifica:
> *Un motto o una frase d'impatto **tra virgolette***

Nel tuo codice hai scritto: `All'attacco!`.
Ti sei chiesto come stampare le virgolette doppie (`"`) senza confondere il compilatore? Se provi a scrivere:
```c
printf(" "All'attacco!" "); // ERRORE!
```
Il compilatore pensa che la stringa finisca subito prima di *All'attacco*. 

Per stampare un carattere speciale come le virgolette dobbiamo usare la **sequenza di escape** anteponendo un backslash: `\"`.
Ecco come si fa:
```c
printf("\"All'attacco!\"\n");
```

---

### 2. Attenzione agli spazi dopo `\n`
Nel tuo testo hai scritto:
```c
"\n *KEVIN* \n *Guerriero* "
```
In C, qualsiasi spazio inserito dopo `\n` viene stampato a video! L'output risulterà indentato di uno spazio a sinistra:
```text
===SCHEDA PERSONAGGIO==
 *KEVIN* 
 *Guerriero* 
```
Se volevi il testo allineato a sinistra, basta togliere lo spazio subito dopo `\n`:
```c
"\n*KEVIN*\n*Guerriero*"
```

---

### 3. Consiglio di stile: leggibilità
Mettere tutto in un'unica riga funziona, ma man mano che i programmi crescono diventa difficile da leggere. Puoi usare più chiamate a `printf` consecutive o andare a capo nel codice:

```c
#include <stdio.h>

int main() {
    printf("=== SCHEDA PERSONAGGIO ===\n");
    printf("Nome: Kevin\n");
    printf("Classe: Guerriero\n");
    printf("Livello: 1\n");
    printf("Motto: \"All'attacco!\"\n"); // Con le virgolette e il \n finale!
    
    return 0;
}
```
*(Nota anche il `\n` alla fine dell'ultima riga: è un'ottima abitudine per evitare che il prompt del terminale si attacchi al tuo testo!)*

---

## Valutazione per il Tutor

**PROMOSSO: pronto per il livello successivo**

*Note di avanzamento:* Lo studente ha compreso perfettamente la struttura fondamentale di un file sorgente C (`#include`, `main`, `return 0`) e l'uso base di `printf` con il ritorno a capo (`\n`). Ha saltato la stampa delle virgolette (probabilmente non conoscendo la sequenza `\"`), argomento che gli è stato spiegato nella correzione. È pronto per affrontare le variabili e i tipi di dato (`int`, `char`, `float`).