import os
import sys
from google import genai

# Inizializza il client Gemini
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# Legge la modalità (daily o review)
mode = sys.argv[1] if len(sys.argv) > 1 else "daily"

# Legge lo stato della sfida attuale e dei progressi passati
challenge_content = ""
if os.path.exists("current_challenge.md"):
    with open("current_challenge.md", "r", encoding="utf-8") as f:
        challenge_content = f.read()

progress_content = ""
if os.path.exists("progress.md"):
    with open("progress.md", "r", encoding="utf-8") as f:
        progress_content = f.read()

if mode == "daily":
    prompt = (
        "Sei un tutor personale di programmazione esperto in C e C++. "
        "Il tuo studente è un principiante assoluto che sta iniziando a imparare il C partendo da zero. "
        "Ecco lo storico dei progressi dello studente fino ad ora:\n"
        f"{progress_content}\n\n"
        "REGOLE PER LA NUOVA SFIDA:\n"
        "1. Analizza i progressi: se lo studente ha superato facilmente gli argomenti precedenti, "
        "proponi un argomento leggermente più avanzato (passando gradualmente da variabili base, input/output, "
        "cicli for/while, funzioni, fino ad arrivare col tempo a puntatori e struct).\n"
        "2. Se invece ha trovato difficoltà, rimani sull'argomento attuale o proponi un esercizio di consolidamento.\n"
        "3. La sfida deve essere pratica, spiegata in modo semplice e adatta a uno studente delle superiori.\n"
        "Scrivi la sfida in Markdown seguendo questa struttura:\n"
        "# Sfida del Giorno\n\n[Titolo e descrizione del problema]\n\n"
        "## Obiettivi\n[Cosa deve fare il programma]\n\n"
        "## La mia soluzione e i miei dubbi\n[Lascia questo spazio vuoto per lo studente]"
    )
else:
    prompt = (
        "Sei un tutor di programmazione C/C++. Lo studente ha inviato la sua soluzione "
        "e i suoi dubbi all'interno di questo file:\n\n"
        f"{challenge_content}\n\n"
        "1. Analizza il codice, individua errori e spiega i concetti in modo chiaro.\n"
        "2. Alla fine della correzione, scrivi una sezione intitolata '## Valutazione per il Tutor' "
        "in cui indichi chiaramente se lo studente ha padroneggiato l'argomento (es. 'PROMOSSO: pronto per il livello successivo') "
        "oppure se ha bisogno di fare altri esercizi simili.\n"
        "Questo testo verrà usato per aggiornare i suoi progressi."
    )

# Chiamata al modello Gemini aggiornato
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=prompt,
)

# Se siamo in modalità daily, salviamo la nuova sfida
if mode == "daily":
    with open("current_challenge.md", "w", encoding="utf-8") as f:
        f.write(response.text)
else:
    # Se siamo in review, aggiungiamo la correzione in fondo al file e aggiorniamo progress.md
    with open("current_challenge.md", "a", encoding="utf-8") as f:
        f.write("\n\n---\n# Correzione del Tutor\n" + response.text)
    
    # Aggiorna il file dei progressi con il feedback
    with open("progress.md", "a", encoding="utf-8") as f:
        f.write(f"\n\n### Revisione recente\n{response.text}")

print("Tutor adattivo eseguito con successo!")