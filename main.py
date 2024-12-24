# main.py file
import tkinter as tk
from wonderwords import RandomSentence
from time import time

s = RandomSentence()
# Texte
sample_text = ""
for phrase in range(1):
    sample_text += s.sentence() + ' '
typed_text = ""
index = 0
timer_started = False
start_time = 0
end_time = 0
numberofchars = len(sample_text) 
wpm = 0
accuracy = numberofchars

# Construction du window
root = tk.Tk()
root.title("Typing Masta")


def reset(): # permet de reset le test
    global index
    index = 0
    text_widget.delete("1.0", tk.END) # supprime le texte écrit
    text_widget.insert("1.0", sample_text) # réinsère le texte
    text_widget.tag_remove("correct", "1.0", tk.END)
    text_widget.tag_remove("incorrect", "1.0", tk.END)


def ecrandefin():
    fin = tk.Toplevel(root)
    fin.title("Fin de la partie")
    fin.geometry("300x200")
    fin.focus_force()
    tk.Label(
        fin,
        text=(
            f"Waza! Vous avez terminé le test. \n"
            f"Mots par minute : {wpm}\n"
            f"Précision : {accuracy}% \n"
            f"Temps écoulé : {end_time - start_time:.2f} seconds"
        )
    ).pack(pady=20)



def on_key(event):
    global index, typed_text, start_time, end_time, timer_started, wpm, accuracy

    if index >= len(sample_text):
        return  # permet de ne pas dépasser la phrase
    
    if timer_started == False and index == 1: # permet de commencer le timer
        timer_started = True
        start_time = time()

    ignored_keys = {"Shift_L", "Shift_R", "Tab", "Caps_Lock", "Alt_L", "Alt_R", "Control_L", "Control_R"}

    if event.keysym in ignored_keys:
        return # ignore les press autre que les lettres, chiffres, etc.
    
    if index > 0 and event.keysym == "BackSpace":
        all_correct = True
        for i in range(index): # pour chaque lettre dans la phrase jusqu<à l'index:
            if 'incorrect' in text_widget.tag_names(f"1.{i}"): # si il y a une lettre incorrecte:
                all_correct = False
                break

        if not all_correct: # si il y a une lettre incorrecte dans le texte precedent,
            index -= 1 # on peut backspace pour supprimer la lettre.
            # recule de 1
            text_widget.tag_remove("correct", f"1.{index}", f"1.{index + 1}")
            text_widget.tag_remove("incorrect", f"1.{index}", f"1.{index + 1}")
        return
    
    typed_char = event.char  # défini chaque press
    if typed_char == sample_text[index]:  # vérifie si le caractère est le même que le sample
        # On attribut "correct" si ==, avec comme range(index, index+1). Fonctionnement: rangée.colonne
        # exemple: 1.0 = indice 0 dans le sample
        text_widget.tag_add("correct", f"1.{index}", f"1.{index + 1}")
        
        if index == len(sample_text) - 2: # for some reason, la longueur du texte a deux chars de trop.
            end_time = time() # arrête le timer
            wpm = round( (numberofchars / 5) / ((end_time - start_time) / 60), 1) # selon la formule du Gross WPM
            
            for i in range(index):
                if 'incorrect' in text_widget.tag_names(f"1.{i}"): # pour chaque index dans la phrase, si il y a une lettre incorrecte, enlever 1 de la précision.
                    accuracy -= 1
            accuracy = round(accuracy / numberofchars * 100, 1)

            ecrandefin() # affiche l'écran de fin
            return

    else:
        # On attribut "incorrect" si !=, avec comme range(index, index+1). Fonctionnement: rangée.colonne
        text_widget.tag_add("incorrect", f"1.{index}", f"1.{index + 1}")


    index += 1  # recommence au next indice





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