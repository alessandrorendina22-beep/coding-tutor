import os
import subprocess
import sys
import json
from datetime import datetime

# File di log locale per lo storico persistente
HISTORY_FILE = "local_history.json"

# Codici ANSI per i colori e lo stile nel terminale
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BLUE = "\033[94m"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.strip()

def load_history():
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def save_history_entry(message):
    history = load_history()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    history.append({
        "date": timestamp,
        "message": message
    })
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=4, ensure_ascii=False)

def show_dashboard():
    clear_screen()
    print(f"{CYAN}╔══════════════════════════════════════════════════════════╗{RESET}")
    print(f"{CYAN}║{RESET} {BOLD}🤖 AI CODING TUTOR — TERMINAL DASHBOARD{RESET}                  {CYAN}║{RESET}")
    print(f"{CYAN}╚══════════════════════════════════════════════════════════╝{RESET}\n")
    
    # 1. Stato Git
    print(f"{YELLOW}📂 STATO WORKSPACE:{RESET}")
    git_status = run_command("git status -s")
    if git_status:
        print(f"  {RED}● Modifiche non salvate o non inviate:{RESET}")
        for line in git_status.split('\n'):
            print(f"    {line}")
    else:
        print(f"  {GREEN}✔ Workspace pulito e sincronizzato con GitHub{RESET}")
    
    print()
    
    # 2. Storico locale con date (JSON)
    print(f"{YELLOW}🕒 STORICO LOCALE (local_history.json):{RESET}")
    history = load_history()
    if history:
        # Mostra gli ultimi 5 invii
        recent_history = history[-5:]
        for entry in recent_history:
            print(f"  {CYAN}[{entry['date']}]{RESET} {entry['message']}")
    else:
        print(f"  {RED}⚠️ Nessun invio registrato nel log locale.{RESET}")
        
    print(f"\n{CYAN}──────────────────────────────────────────────────────────{RESET}")
    input(f"\n{BOLD}Premi INVIO per tornare al menu principale...{RESET}")

def main():
    while True:
        clear_screen()
        print(f"{CYAN}╔══════════════════════════════════════════════════════════╗{RESET}")
        print(f"{CYAN}║{RESET} {BOLD}⚡ C/C++ AI TUTOR MANAGER v3.0 (Local JSON){RESET}             {CYAN}║{RESET}")
        print(f"{CYAN}╚══════════════════════════════════════════════════════════╝{RESET}\n")
        
        print(f"  {GREEN}[1]{RESET} 📊 Apri Dashboard e Storico Locale")
        print(f"  {GREEN}[2]{RESET} 🚀 Invia Soluzione (Git Commit & Push + Log)")
        print(f"  {GREEN}[3]{RESET} 🔄 Sincronizza con GitHub (Git Pull)")
        print(f"  {RED}[4]{RESET} 🚪 Esci\n")
        
        choice = input(f"{BOLD}👉 Scegli un'opzione [1-4]: {RESET}").strip()
        
        if choice == "1":
            show_dashboard()
        elif choice == "2":
            clear_screen()
            print(f"{CYAN}--- 🚀 INVIO SOLUZIONE & REGISTRAZIONE LOG ---{RESET}\n")
            status = run_command("git status --porcelain")
            if status or os.path.exists("current_challenge.md"):
                run_command("git add current_challenge.md")
                if os.path.exists("manager.py"):
                    run_command("git add manager.py")
                if os.path.exists(HISTORY_FILE):
                    run_command(f"git add {HISTORY_FILE}")
                    
                msg = input(f"{YELLOW}Inserisci un breve commento sulla soluzione: {RESET}").strip()
                if not msg: 
                    msg = "Soluzione inviata dallo studente"
                
                # Salva nel file JSON locale con data e ora
                save_history_entry(msg)
                
                print(f"\n{BLUE}⏳ Esecuzione commit, push e aggiornamento log...{RESET}")
                run_command(f'git commit -m "{msg}"')
                run_command("git push")
                print(f"\n{GREEN}✨ Soluzione inviata e log salvato con successo!{RESET}")
            else:
                print(f"{YELLOW}⚠️ Nessuna modifica trovata da inviare!{RESET}")
            input(f"\n{BOLD}Premi INVIO per continuare...{RESET}")
        elif choice == "3":
            clear_screen()
            print(f"{CYAN}--- 🔄 SINCRONIZZAZIONE ---{RESET}\n")
            print(f"{BLUE}⏳ Scaricamento aggiornamenti da GitHub...{RESET}")
            res = run_command("git pull")
            print(res)
            print(f"\n{GREEN}✔ Sincronizzazione completata!{RESET}")
            input(f"\n{BOLD}Premi INVIO per continuare...{RESET}")
        elif choice == "4":
            clear_screen()
            print(f"{GREEN}Buono studio! Alla prossima sessione di codice. 👋{RESET}\n")
            break
        else:
            print(f"\n{RED}❌ Scelta non valida. Inserisci un numero da 1 a 4.{RESET}")
            input(f"\nPremi INVIO per riprovare...")

if __name__ == "__main__":
    main()