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