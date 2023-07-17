from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=400, height=400)
logo = PhotoImage(file='logo.png')
canvas.create_image(200, 200, image=logo)
canvas.pack()

window.mainloop()
