import os
import subprocess
import sys

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
    
    # 2. Ultimi progressi
    print(f"{YELLOW}📊 ULTIMI PROGRESSI (progress.md):{RESET}")
    if os.path.exists("progress.md"):
        with open("progress.md", "r", encoding="utf-8") as f:
            lines = f.readlines()
            # Mostra le ultime 8 righe in modo pulito
            recent_lines = lines[-8:] if len(lines) >= 8 else lines
            for line in recent_lines:
                print(f"  │ {line.strip()}")
    else:
        print(f"  {RED}⚠️ File progress.md non ancora trovato.{RESET}")
        
    print(f"\n{CYAN}──────────────────────────────────────────────────────────{RESET}")
    input(f"\n{BOLD}Premi INVIO per tornare al menu principale...{RESET}")

def main():
    while True:
        clear_screen()
        print(f"{CYAN}╔══════════════════════════════════════════════════════════╗{RESET}")
        print(f"{CYAN}║{RESET} {BOLD}⚡ C/C++ AI TUTOR MANAGER v2.0{RESET}                          {CYAN}║{RESET}")
        print(f"{CYAN}╚══════════════════════════════════════════════════════════╝{RESET}\n")
        
        print(f"  {GREEN}[1]{RESET} 📊 Apri Dashboard e Storico")
        print(f"  {GREEN}[2]{RESET} 🚀 Invia Soluzione (Git Commit & Push)")
        print(f"  {GREEN}[3]{RESET} 🔄 Sincronizza con GitHub (Git Pull)")
        print(f"  {RED}[4]{RESET} 🚪 Esci\n")
        
        choice = input(f"{BOLD}👉 Scegli un'opzione [1-4]: {RESET}").strip()
        
        if choice == "1":
            show_dashboard()
        elif choice == "2":
            clear_screen()
            print(f"{CYAN}--- 🚀 INVIO SOLUZIONE ---{RESET}\n")
            status = run_command("git status --porcelain")
            if status:
                run_command("git add current_challenge.md")
                msg = input(f"{YELLOW}Inserisci un breve commento sulla soluzione: {RESET}").strip()
                if not msg: 
                    msg = "Soluzione inviata dallo studente"
                
                print(f"\n{BLUE}⏳ Esecuzione commit e push in corso...{RESET}")
                run_command(f'git commit -m "{msg}"')
                run_command("git push")
                print(f"\n{GREEN}✨ Push completato con successo su GitHub!{RESET}")
            else:
                print(f"{YELLOW}⚠️ Nessuna modifica trovata in current_challenge.md da inviare!{RESET}")
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