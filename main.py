import tkinter as tk
from wonderwords import RandomSentence
from time import time

sample_text = ""
typed_text = ""
index = 0
timer_started = False
start_time = 0
end_time = 0
numberofchars = 0
wpm = 0
accuracy = numberofchars
difficulty = None

s = RandomSentence()
# Texte
def texte_facile():
    liste = []
    for phrase in range(1):
        liste.append(s.sentence())
    return " ".join(liste)

def texte_moyen():
    liste = []
    for phrase in range(3):
        liste.append(s.sentence())
    return " ".join(liste)

def texte_difficile():
    liste = []
    for phrase in range(5):
        liste.append(s.sentence())
    return " ".join(liste)

# Création du widget de texte et ses configurations (tags)
def setup_text_widget(text_function):
    global text_widget, sample_text, numberofchars, accuracy, difficulty
    clear()
    text_widget = tk.Text(mainframe, height=5, width=50, font=("Arial", 16), wrap="word")
    text_widget.pack(pady=10)
    
    # Définir la difficulté actuelle
    if text_function == texte_facile:
        difficulty = "easy"
    elif text_function == texte_moyen:
        difficulty = "medium"
    elif text_function == texte_difficile:
        difficulty = "hard"


    # text_function() peut être texte_facile(), texte_moyen() ou texte_difficile() lorsque appelée. (lignes 17-29)
    sample_text = text_function()
    numberofchars = len(sample_text)
    accuracy = numberofchars
    text_widget.insert("1.0", sample_text)
    
    text_widget.config(state="disabled")
    text_widget.tag_config("correct", foreground="green")
    text_widget.tag_config("incorrect", foreground="red")
    
    # Boutons back et reset
    backbtn = tk.Button(mainframe, text="Retour", command=mainmenu)
    backbtn.pack(pady=10)
    resetbtn = tk.Button(mainframe, text="Reset", command=reset)
    resetbtn.pack(pady=10)
    
    root.bind("<KeyRelease>", on_key)

def texte_suivant():
    # réinitialiser tout, donc texte_suivant est en quelque sorte aussi un reset
    global sample_text, index, numberofchars, accuracy, start_time, end_time, timer_started, difficulty
    
    if difficulty == "easy":
        sample_text = texte_facile()
    elif difficulty == "medium":
        sample_text = texte_moyen()
    elif difficulty == "hard":
        sample_text = texte_difficile()

    index = 0
    numberofchars = len(sample_text)
    accuracy = numberofchars
    start_time = 0
    end_time = 0
    timer_started = False

    text_widget.config(state="normal")  # Permettre les modifications
    text_widget.delete("1.0", tk.END)  # Supprimer le texte précédent
    text_widget.insert("1.0", sample_text)  # Insérer le nouveau texte
    text_widget.tag_remove("correct", "1.0", tk.END)  # Supprimer les tags "correct"
    text_widget.tag_remove("incorrect", "1.0", tk.END)  # Supprimer les tags "incorrect"
    text_widget.config(state="disabled")  # Désactiver l'édition du texte



# Construction du window
root = tk.Tk()
root.title("Typing Masta")
root.geometry("800x600")
root.iconbitmap("typingmasta/tlogo.ico") # changer le logo
titlelabel = tk.Label(root, text="Typing Masta", font=("Arial", 24))
titlelabel.pack(pady=10)
subtitle = tk.Label(root, text="Testez votre vitesse de frappe!", font=("Arial", 16))
subtitle.pack(pady=10)
mainframe = tk.Frame(root)
mainframe.pack(pady=10)

def clear():
    for widget in mainframe.winfo_children():
        widget.destroy()

def mainmenu():
    clear()
    easybtn = tk.Button(mainframe, command=easy, text="Facile", font=("Arial", 16), width=10, height=2, bg="green", fg="white")
    mediumbtn = tk.Button(mainframe, command=medium, text="Moyen", font=("Arial", 16), width=10, height=2, bg="orange", fg="white")
    hardbtn = tk.Button(mainframe, command=hard, text="Difficile", font=("Arial", 16), width=10, height=2, bg="red", fg="white")
    quitbtn = tk.Button(mainframe, text="Quitter", command=root.quit, font=("Arial", 16), width=10, height=2, bg="black", fg="white")
    easybtn.pack(pady=10)
    mediumbtn.pack(pady=10)
    hardbtn.pack(pady=10)
    quitbtn.pack(pady=10)

def easy():
    setup_text_widget(texte_facile)

def medium():
    setup_text_widget(texte_moyen)

def hard():
    setup_text_widget(texte_difficile)

def reset(): # permet de reset le test
    global index, numberofchars, accuracy, start_time, end_time, timer_started, text_widget
    index = 0
    text_widget.delete("1.0", tk.END) # supprime le texte écrit
    text_widget.insert("1.0", sample_text) # réinsère le texte
    text_widget.tag_remove("correct", "1.0", tk.END)
    text_widget.tag_remove("incorrect", "1.0", tk.END)
    numberofchars = len(sample_text)
    accuracy = numberofchars
    start_time = 0
    end_time = 0
    timer_started = False
    
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
            f"Temps écoulé : {end_time - start_time:.2f} secondes"
        )
    ).pack(pady=20)
    tk.Button(fin, text="reset", command=lambda: (reset(), fin.destroy())).pack(side=tk.LEFT, fill=tk.X, padx=75) # implémentation du bouton reset
    tk.Button(fin, text="next", command=lambda: (texte_suivant(), fin.destroy())).pack(side=tk.LEFT, fill=tk.X) # implémentation du bouton next



# Fonction appelée à chaque key press du clavier
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


    if index == len(sample_text) - 1: # si on atteint la fin de la phrase

        if typed_char == sample_text[index]: # si la lettre est correcte, on ajoute le tag correct
            text_widget.tag_add("correct", f"1.{index}", f"1.{index + 1}")
        else: # sinon, on ajoute le tag incorrect
            text_widget.tag_add("incorrect", f"1.{index}", f"1.{index + 1}")

        end_time = time() # arrête le timer
        wpm = round( (numberofchars / 5) / ((end_time - start_time) / 60), 1) # selon la formule du Gross WPM
            
        for i in range(index):
            if 'incorrect' in text_widget.tag_names(f"1.{i}"): # pour chaque index dans la phrase, si il y a une lettre incorrecte, enlever 1 de la précision.
                accuracy -= 1
        accuracy = round(accuracy / numberofchars * 100, 1)

        ecrandefin() # affiche l'écran de fin
        return

    # Gestion normale des tags si on a pas atteint la fin de la phrase.
    if typed_char == sample_text[index]:
        text_widget.tag_add("correct", f"1.{index}", f"1.{index + 1}")
    else:
        # On attribut "incorrect" si !=, avec comme range(index, index+1). Fonctionnement: rangée.colonne
        text_widget.tag_add("incorrect", f"1.{index}", f"1.{index + 1}")


    index += 1  # recommence au next indice


# Esthétique du message


# Définir les couleurs à vert et rouge pour correct et incorrect respectivement


# Crée une action à chaque press du clavier
root.bind("<KeyRelease>", on_key)

# Création du button reset

mainmenu()
# Jouer la loop
root.mainloop()