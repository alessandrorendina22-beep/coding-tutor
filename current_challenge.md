# Sfida del Giorno

### Registro Voti Dinamico (C / C++)

Ciao! Oggi metteremo alla prova le tue competenze su tre dei concetti più importanti e temuti della programmazione a basso livello: **struct**, **puntatori** e **gestione dinamica della memoria** (`malloc`/`free` in C o `new`/`delete` in C++).

Immagina di dover creare il nucleo di un registro scolastico. Il programma non conosce a priori il numero di studenti della classe: questo dato verrà inserito dall'utente all'avvio. Dovrai allocare lo spazio necessario a runtime, raccogliere i dati, trovare lo studente con il rendimento migliore e assicurarti di non lasciare alcun *memory leak*.

---

## Obiettivi

1. **Definisci la `struct Studente`:**
   - `nome`: stringa (array di `char` di dimensione massima 50).
   - `matricola`: intero.
   - `media`: float (compresa tra 2.0 e 10.0).

2. **Allocazione Dinamica:**
   - Chiedi all'utente quanti studenti ($N$) compongono la classe.
   - Alloca dinamicamente memoria sufficiente a contenere l'array di $N$ studenti.
   - Verifica sempre che l'allocazione sia andata a buon fine.

3. **Funzioni con Puntatori:**
   - Implementa una funzione per l'inserimento dei dati:  
     `void inserisciDati(Studente* classe, int n);`
   - Implementa una funzione per trovare lo studente migliore, che restituisca un **puntatore** all'elemento trovato:  
     `Studente* trovaMigliore(Studente* classe, int n);`
   - Implementa una funzione per calcolare la media generale della classe:  
     `float calcolaMediaClasse(const Studente* classe, int n);`

4. **Stampa e Gestione della Memoria:**
   - Nel `main`, mostra i dati dello studente con la media più alta (accedendovi tramite il puntatore restituito) e la media totale della classe.
   - **Fondamentale:** Dealloca correttamente tutta la memoria dinamica prima del termine del programma.

*Bonus (facoltativo):* Prova a scrivere il codice in C puro o in C++ moderno a tua scelta, specificando quale standard hai scelto di seguire!

---

## La mia soluzione e i miei dubbi

*(Incolla qui il tuo codice e scrivi le domande o i passaggi che non ti sono del tutto chiari)*