from tkinter import *

window = Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a Label", font=("Ariel", 24))
my_label.pack()

my_label["text"] = "New Text"

# Button

def button_clicked():
    print("I got clicked!")
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
input = Entry(width=10)
input.pack()








window.mainloop()
