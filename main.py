# main.py file
import tkinter as tk
<<<<<<< HEAD
from wonderwords import RandomSentence


s = RandomSentence()
# Texte
sample_text = ""
for phrase in range(5):
    sample_text += s.sentence() + '\n'

index = 0
no_phrase = 1

def on_key(event):
    global index # Permet de modifier la variable "index" en tant que variable global
    if index >= len(sample_text):
        return  # permet de ne pas dépasser la phrase
    
    ignored_keys = {"Shift_L", "Shift_R", "Tab", "Caps_Lock", "Alt_L", "Alt_R", "Control_L", "Control_R"}
    if event.keysym in ignored_keys:
        return # ignore les press autre que les lettres, chiffres, etc.
    
    if index > 0 and event.keysym == "BackSpace":
        index -= 1
        # recule de 1
        text_widget.tag_remove("correct", f"{no_phrase}.{index}", f"{no_phrase}.{index + 1}")
        text_widget.tag_remove("incorrect", f"{no_phrase}.{index}", f"{no_phrase}.{index + 1}")
        return # supprime la couleur
    
    typed_char = event.char  # défini chaque press
    if typed_char == sample_text[index]:  # vérifie si le caractère est le même que le sample
        # On attribut "correct" si ==, avec comme range(index, index+1). Fonctionnement: rangée.colonne
        # exemple: 1.0 = indice 0 dans le sample
        text_widget.tag_add("correct", f"{no_phrase}.{index}", f"{no_phrase}.{index + 1}")
    else:
        # On attribut "incorrect" si !=, avec comme range(index, index+1). Fonctionnement: rangée.colonne
        text_widget.tag_add("incorrect", f"{no_phrase}.{index}", f"{no_phrase}.{index + 1}")

    index += 1  # recommence au next indice

def reset(): # permet de reset le test
    global index
    index = 0
    text_widget.delete("1.0", tk.END) # supprime le texte écrit
    text_widget.insert("1.0", sample_text) # réinsère le texte
    text_widget.tag_remove("correct", "1.0", tk.END)
    text_widget.tag_remove("incorrect", "1.0", tk.END)

# Construction du window
root = tk.Tk()
root.title("Typing Masta")

# Esthétique du message
text_widget = tk.Text(root, height=5, width=50, font=("Arial", 16), wrap="word")
text_widget.pack(pady=10)
text_widget.insert("1.0", sample_text)
text_widget.config(state="disabled")  # Empêche l'utilisateur d'éditer le message

# Définir les couleurs à vert et rouge pour correct et incorrect respectivement
text_widget.tag_config("correct", foreground="green")
text_widget.tag_config("incorrect", foreground="red")

# Crée une action à chaque press du clavier
root.bind("<KeyRelease>", on_key)

# Création du button reset
reset_button = tk.Button(root, text="Reset", command=reset)
reset_button.pack(pady=10)

# Jouer la loop
root.mainloop()
=======

# creation of a 800x600 TK window called Typing Masta.
window = tk.Tk()
window.geometry("800x600")
window.title("Typing Masta")

# This is the text we are gonna be showing as a label on the window (the text to write.)
custom_text = "Hello, this is a typing test."

# function to update the custom_text characters at every event.
def update_paragraph(event):
    global typed_text
    
    # typed_text is updated with event.char (which is the character entered on the keyboard.)
    typed_text += event.char
    
    new_text = typed_text + custom_text[len(typed_text):]
    Paragraph.config(text=new_text)

# Creation of the paragraph with the custom_text showed on the window.
Paragraph = tk.Label(window, text=custom_text, font=("Helvetica", 50), fg="grey", width=0)
Paragraph.place(relx=0.5, rely=0.5, anchor="center")

typed_text = ""

# This line tells that, when any keyboard key is pressed, upon release,
# trigger the update_paragraph function, which updates the Paragraph label.
window.bind('<KeyRelease>', update_paragraph)

window.mainloop()
>>>>>>> 9d83c8ac64221f2a610ac095896e91996510dd33
