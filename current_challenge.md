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
// Incolla qui il tuo codice


```

*(Scrivi qui eventuali dubbi, errori del compilatore o domande che ti sono venute mentre programmavi)*