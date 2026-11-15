import os
import sys
from google import genai

# Inizializza il client Gemini con la chiave presa dalle variabili d'ambiente
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# Legge la modalità (daily o review) passata da riga di comando
mode = sys.argv[1] if len(sys.argv) > 1 else "daily"

# Legge lo stato attuale dei file se esistono
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
        "Genera una nuova sfida di programmazione pratica adatta a uno studente delle superiori "
        "che studia informatica. La sfida deve concentrarsi su argomenti come: puntatori, "
        "gestione della memoria, array, struct o algoritmi in C/C++. "
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
        "Analizza il codice, individua eventuali errori, spiega i concetti in modo chiaro "
        "e scrivi una correzione costruttiva in fondo al file."
    )

# Chiamata al modello Gemini aggiornato
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=prompt,
)

# Scrive il risultato direttamente dentro current_challenge.md
with open("current_challenge.md", "w", encoding="utf-8") as f:
    f.write(response.text)

print("Tutor eseguito con successo e file aggiornato!")