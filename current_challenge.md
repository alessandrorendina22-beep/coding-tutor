# Sfida del Giorno

### Benvenuto nel C: Crea la tua "Scheda Personaggio"!

Ciao! Benvenuto nel fantastico mondo della programmazione in C. Il C è un linguaggio potente, veloce e alla base di tantissimi sistemi moderni (come i sistemi operativi e i motori grafici dei videogiochi!).

Per iniziare il nostro percorso partiremo dalle fondamenta assolute: la struttura di base di un programma C e come far "parlare" il computer sullo schermo usando la funzione `printf`.

Immagina di dover creare la schermata iniziale per un gioco di ruolo: il tuo primo compito è stampare a video la scheda del tuo personaggio!

---

## Obiettivi

Scrivi un programma in C che:
1. Includa la libreria standard fondamentale per mostrare testo a schermo (`<stdio.h>`).
2. Contenga la funzione principale da cui tutto ha inizio (`main`).
3. Usi il comando `printf` e il carattere speciale di "a capo" (`\n`) per stampare su righe diverse:
   - Un titolo decorativo (es. `=== SCHEDA PERSONAGGIO ===`)
   - Il nome del tuo personaggio
   - La sua classe o ruolo (es. *Guerriero*, *Hacker*, *Mago*)
   - Il suo livello iniziale (es. *Livello: 1*)
   - Un motto o una frase d'impatto tra virgolette
4. Concluda correttamente il programma restituendo il valore `0`.

---

## La mia soluzione e i miei dubbi

```c
#include <stdio.h>

int main(){
   printf("===SCHEDA PERSONAGGIO==\n *KEVIN* \n *Guerriero* \n *Livello 1* \n All'attacco!");
   return 0;
}
```

**Non ho trovato difficile nulla!**
- 

---
# Correzione del Tutor
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