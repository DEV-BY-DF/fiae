import tkinter as tk
from tkinter import messagebox
import random

fragen = [
    {"frage": "Was bedeutet die Abkürzung CPU?", "optionen": ["Central Processing Unit", "Cash Printing Uwu", "Complex Problems Unlimited", "Creamy Pie Utilizer"], "antwort": "Central Processing Unit"},
    {"frage": "Welche der folgenden Datentypen ist in SQL gültig?", "optionen": ["float", "boolean", "varchar", "string"], "antwort": "varchar"},
    {"frage": "Welche Schleife prüft die Bedingung erst nach dem ersten Durchlauf?", "optionen": ["for", "while", "do-while", "foreach"], "antwort": "do-while"},
    {"frage": "Welche IP-Adresse gehört zum privaten Bereich?", "optionen": ["8.8.8.8", "192.168.1.1", "172.0.0.1", "224.0.0.1"], "antwort": "192.168.1.1"},
    {"frage": "Was ist ein Primärschlüssel in einer Datenbank?", "optionen": ["Ein eindeutiges Attribut", "Ein Schlüssel zur Verschlüsselung", "Ein Index", "Ein Sekundärattribut"], "antwort": "Ein eindeutiges Attribut"},
    {"frage": "Welcher Port wird standardmäßig für HTTP verwendet?", "optionen": ["21", "22", "80", "443"], "antwort": "80"},
    {"frage": "Was beschreibt ein Algorithmus?", "optionen": ["Einen Ablaufplan", "Eine Hardware-Komponente", "Ein Betriebssystem", "Eine Tabellenstruktur"], "antwort": "Einen Ablaufplan"},
    {"frage": "Welche Aussage zu Open Source ist korrekt?", "optionen": ["Der Quellcode ist geheim", "Jede Nutzung ist verboten", "Der Quellcode ist öffentlich", "Nur Unternehmen dürfen Open Source nutzen"], "antwort": "Der Quellcode ist öffentlich"},
    {"frage": "Welcher der folgenden Begriffe steht für ein Versionskontrollsystem?", "optionen": ["Git", "Ping", "Node.js", "CMD"], "antwort": "Git"},
    {"frage": "Wofür steht das 'T' in HTTP?", "optionen": ["Transfer", "Tool", "Text", "Transaction"], "antwort": "Transfer"},
    {"frage": "Was ist ein Compiler?", "optionen": ["Ein Übersetzer für Quellcode", "Ein Testprogramm", "Ein Debugger", "Ein Editor"], "antwort": "Ein Übersetzer für Quellcode"},
    {"frage": "Was gehört nicht zum EVA-Prinzip?", "optionen": ["Eingabe", "Verarbeitung", "Ausgabe", "Verwaltung"], "antwort": "Verwaltung"},
    {"frage": "Was bedeutet DRY in der Softwareentwicklung?", "optionen": ["Don’t Repeat Yourself", "Deploy Runtime Yield", "Direct Runtime YAML", "Double Runtime Yes"], "antwort": "Don’t Repeat Yourself"},
    {"frage": "Welcher Datentyp ist geeignet für Fließkommazahlen in Python?", "optionen": ["int", "str", "bool", "float"], "antwort": "float"},
    {"frage": "Was ist eine IDE?", "optionen": ["Ein Compiler", "Ein Server", "Eine Entwicklungsumgebung", "Ein Datenformat"], "antwort": "Eine Entwicklungsumgebung"},
    {"frage": "Welcher der folgenden ist KEIN logischer Operator?", "optionen": ["AND", "OR", "NOT", "THEN"], "antwort": "THEN"},
    {"frage": "Wie beginnt man in SQL eine neue Tabelle?", "optionen": ["MAKE TABLE", "CREATE TABLE", "BUILD TABLE", "SET TABLE"], "antwort": "CREATE TABLE"},
    {"frage": "Was ist das Ziel von Normalformen in der Datenbankentwicklung?", "optionen": ["Datenmengen erhöhen", "Redundanz vermeiden", "System schneller machen", "Komplexität erhöhen"], "antwort": "Redundanz vermeiden"},
    {"frage": "Was bedeutet das Kürzel LAN?", "optionen": ["Large Area Network", "Local Access Node", "Local Area Network", "Layer Access Network"], "antwort": "Local Area Network"},
    {"frage": "Welche Datei-Endung ist typisch für ein Python-Skript?", "optionen": [".pyc", ".pyt", ".py", ".pt"], "antwort": ".py"}
]

class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("IHK-Prüfung Lernkarten")
        self.geometry("800x600")
        self.configure(bg="#f0f2f5")
        
        # Quiz-Einstellungen
        self.total_fragen = len(fragen)
        self.current_index = 0
        self.score = 0
        self.learned = 0
        
        # UI aufbauen
        self.create_header()
        self.create_card_frame()
        self.create_card_label()
        self.create_question_label()
        self.create_answer_buttons()
        self.create_navigation_buttons()
        
        # Erstes Laden der Fragen
        self.shuffle_questions()

    def create_header(self):
        header = tk.Frame(self, bg="#f0f2f5", padx=20, pady=10)
        header.pack(fill="x")
        tk.Label(header, text="Learn for AP's", font=("Arial", 24, "bold"), bg="#f0f2f5").pack()
        tk.Label(header, text="Fachinformatiker für Anwendungsentwicklung", font=("Arial", 12), bg="#f0f2f5").pack()

    def create_card_frame(self):
        self.card_frame = tk.Frame(self, bg="white", padx=20, pady=20)
        self.card_frame.pack(fill="both", expand=True, padx=40, pady=20)

    def create_card_label(self):
        frame = tk.Frame(self.card_frame, bg="white")
        frame.pack(fill="x")
        self.card_label = tk.Label(frame, text=f"Karte: 1/{self.total_fragen}", font=("Arial", 12), bg="white")
        self.card_label.pack(side="left", padx=20)

    def create_question_label(self):
        self.question_label = tk.Label(
            self.card_frame, text="", bg="#303ca5", fg="white",
            font=("Arial", 20), wraplength=700, pady=40
        )
        self.question_label.pack(fill="both", padx=20, pady=20)

    def create_answer_buttons(self):
        self.option_buttons = []
        frame = tk.Frame(self.card_frame, bg="white")
        frame.pack(pady=20)
        for i in range(4):
            btn = tk.Button(
                frame, text="", bg="#e8e8e8", fg="#333", font=("Arial", 14),
                width=50, relief="flat",
                command=lambda idx=i: self.check_answer(idx)
            )
            btn.pack(pady=5)
            self.option_buttons.append(btn)

    def create_navigation_buttons(self):
        frame = tk.Frame(self, bg="#f0f2f5")
        frame.pack(pady=20)
        tk.Button(frame, text="Zurück", bg="#4a90e2", fg="white", font=("Arial", 14), relief="flat", command=self.prev_question).pack(side="left", padx=10)
        tk.Button(frame, text="Als gelernt markieren", bg="#2ecc71", fg="white", font=("Arial", 14), relief="flat", command=self.mark_as_learned).pack(side="left", padx=10)
        tk.Button(frame, text="Weiter", bg="#5a75cd", fg="white", font=("Arial", 14), relief="flat", command=self.next_question).pack(side="left", padx=10)

    def shuffle_questions(self):
        random.shuffle(fragen)
        self.current_index = 0
        self.score = 0
        self.update_question()

    def update_question(self):
        if self.current_index < self.total_fragen:
            q = fragen[self.current_index]
            # Frage und Antworten setzen
            self.question_label.config(text=q["frage"])
            opts = q["optionen"].copy()
            random.shuffle(opts)
            for btn, opt in zip(self.option_buttons, opts):
                btn.config(text=opt, bg="#e8e8e8", state=tk.NORMAL)
            # Kartennummer aktualisieren
            self.card_label.config(text=f"Karte: {self.current_index+1}/{self.total_fragen}")
        else:
            self.show_completion_message()

    def check_answer(self, idx):
        selected = self.option_buttons[idx].cget("text")
        correct = fragen[self.current_index]["antwort"]
        # Feedback
        color = "#90ee90" if selected == correct else "#ff7f7f"
        self.option_buttons[idx].config(bg=color)
        if selected == correct:
            self.score += 1
        for btn in self.option_buttons:
            btn.config(state=tk.DISABLED)
        self.after(800, self.next_question)

    def next_question(self):
        self.current_index += 1
        self.update_question()

    def prev_question(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.update_question()

    def mark_as_learned(self):
        self.learned += 1

    def show_completion_message(self):
        messagebox.showinfo("Quiz abgeschlossen", f"Sie haben {self.score} von {self.total_fragen} korrekt beantwortet.")
        self.destroy()

if __name__ == "__main__":
    QuizApp().mainloop()
