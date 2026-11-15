import os
import subprocess
import sys

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.strip()

def show_dashboard():
    print("\n" + "="*50)
    print(" 🚀 CODING TUTOR TERMINAL DASHBOARD - STATS & ANALYTICS ")
    print("="*50)
    
    # Legge il file di progresso se esiste
    if os.path.exists("progress.md"):
        print("\n📊 ULTIMI PROGRESSI REGISTRATI:")
        with open("progress.md", "r", encoding="utf-8") as f:
            lines = f.readlines()
            # Mostra le ultime 10 righe significative o una panoramica
            print("".join(lines[-15:]))
    else:
        print("\n⚠️ File progress.md non ancora trovato. Completa la prima sfida!")
        
    print("-" * 50)
    print("🔍 STATO ATTUALE:")
    git_status = run_command("git status -s")
    if git_status:
        print("Modifiche non ancora inviate:")
        print(git_status)
    else:
        print("Workspace pulito e sincronizzato con GitHub ✅")
    print("="*50 + "\n")

def main():
    while True:
        print("\n--- 🤖 MENU PRINCIPALE TUTOR ---")
        print("1. 📊 Visualizza Dashboard e Storico nel Terminale")
        print("2. 🚀 Invia Soluzione (Git Commit & Push)")
        print("3. 🔄 Sincronizza (Git Pull)")
        print("4. 🚪 Esci")
        
        choice = input("\nScegli un'opzione (1-4): ").strip()
        
        if choice == "1":
            show_dashboard()
        elif choice == "2":
            status = run_command("git status --porcelain")
            if status:
                run_command("git add current_challenge.md")
                msg = input("Inserisci un commento sulla soluzione: ").strip()
                if not msg: msg = "Soluzione inviata"
                run_command(f'git commit -m "{msg}"')
                run_command("git push")
                print("✨ Push completato con successo!")
            else:
                print("Nessuna modifica da inviare!")
        elif choice == "3":
            run_command("git pull")
            print("🔄 Sincronizzazione completata!")
        elif choice == "4":
            print("Alla prossima sessione di codice! Ciao!")
            break
        else:
            print("Scelta non valida, riprova.")

if __name__ == "__main__":
    main()