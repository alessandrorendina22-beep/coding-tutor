# Sfida del Giorno

### Livello 3: Il Conto alla Taverna del Drago (L'Input dell'Utente con `scanf`)

Finora i tuoi programmi hanno lavorato con valori "fissi", scritti direttamente nel codice (chiamati in gergo *hardcoded*). Ma la vera magia della programmazione inizia quando il programma diventa **interattivo**, cioè capace di ascoltare l'utente e reagire a ciò che scrive sulla tastiera!

Per fare questo in C usiamo una funzione "gemella" di `printf`: **`scanf`** (che sta per *scan formatted*, ovvero "fai la scansione di dati formattati").

Ecco come funziona:
```c
int eta;
printf("Quanti anni hai? ");
scanf("%d", &eta); // Attenzione a quella & !
```

Noti qualcosa di strano? Davanti al nome della variabile c'è il simbolo **`&`** (la e commerciale, o *ampersand*).
Perché serve? 
Mentre `printf` ha solo bisogno di *leggere* il valore di una variabile per mostrarlo a schermo, `scanf` deve andare a *scrivere* il dato dentro la memoria del computer. Il simbolo `&` indica **l'indirizzo di memoria** della variabile: in pratica dice a `scanf` *"Ehi, prendi il numero digitato dall'utente e vallo a infilare esattamente nella scatola di `eta`!"*.

---

### Lo Scenario
Sei alla *Taverna del Drago* con il tuo gruppo di avventurieri dopo una lunga missione. Il locandiere vi porta il conto totale del banchetto, ma tocca a te fare i conti e stabilire quanto deve sborsare ogni membro del gruppo per dividere equamente la spesa!

---

## Obiettivi

Crea un programma in C che:

1. **Dichiari le variabili necessarie:**
   - Un intero per il numero di avventurieri (es. `int avventurieri;`).
   - Un decimale per la spesa totale (es. `float conto_totale;`).
   - Un decimale per la quota individuale (es. `float quota_singola;`).

2. **Chieda i dati all'utente in modo interattivo:**
   - Mostri un messaggio di richiesta con `printf` (es. `"Quanti avventurieri siete al tavolo? "`).
   - Usi `scanf` per leggere il numero intero inserito dall'utente.
   - Mostri un secondo messaggio (es. `"A quanto ammonta il conto totale in monete d'oro? "`).
   - Usi `scanf` con `%f` e la `&` per leggere il valore decimale.

3. **Esegua il calcolo:**
   - Calcoli la quota a testa dividendo il conto totale per il numero di avventurieri (`conto_totale / avventurieri`).

4. **Stampi il riepilogo:**
   - Mostri a video un riassunto ordinato con la spesa totale e la quota esatta che ogni avventuriero deve pagare, formattando le monete con **due cifre decimali** (`%.2f`).
   - Concluda il programma con `return 0;`.

*Esempio di come dovrebbe apparire il terminale durante l'esecuzione:*
```text
=== TAVERNA DEL DRAGO ===
Quanti avventurieri siete al tavolo? 4
A quanto ammonta il conto totale? 54.50

--- DIVISIONE DEL CONTO ---
Conto totale: 54.50 monete
Ogni avventuriero deve pagare: 13.62 monete d'oro.
```

---

## La mia soluzione e i miei dubbi

```c
// Incolla qui il tuo codice


```

*(Scrivi pure qui sotto eventuali dubbi o comportamenti del codice che non ti convincono!)*