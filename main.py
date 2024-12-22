# main.py file
import tkinter as tk

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