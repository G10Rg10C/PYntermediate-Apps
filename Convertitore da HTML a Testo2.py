import tkinter as tk
from tkinter import scrolledtext
from bs4 import BeautifulSoup

# Funzione per tradurre HTML in testo e rimuovere spazi superflui
def traduci_html():
    # Recupera il contenuto HTML dalla textbox a sinistra
    html_content = input_text.get("1.0", tk.END)
    # Utilizza BeautifulSoup per estrarre il testo leggibile
    soup = BeautifulSoup(html_content, "html.parser")
    readable_text = soup.get_text(separator="\n")
    # Rimuove righe vuote e spazi superflui
    cleaned_text = "\n".join(line.strip() for line in readable_text.splitlines() if line.strip())
    # Inserisce il testo tradotto nella textbox a destra
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, cleaned_text)

# Creazione della finestra principale
root = tk.Tk()
root.title("Convertitore HTML -> Testo")
root.geometry("800x600")

# Configurazione delle colonne
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=0)
root.columnconfigure(2, weight=1)

# Textbox per l'input HTML
input_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50)
input_text.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Pulsante per la traduzione
translate_button = tk.Button(root, text="Traduci", command=traduci_html, width=15, bg="#007acc", fg="white")
translate_button.grid(row=0, column=1, padx=5, pady=10)

# Textbox per il risultato tradotto
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50)
output_text.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

# Avvia il loop principale dell'interfaccia
root.mainloop()
