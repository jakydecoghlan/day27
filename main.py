from tkinter import *

window = Tk()

window.title("Mi primera GUI")
window.minsize(width=500, height=300)

#Label

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0)
my_label.config(text="New Text")

#Button

def tralala():
    print("Uh, you touched my tralalá")
    my_label.config(text=input.get())

Button = Button(text="Click Me", command=tralala)
Button.pack()

#Entry
input = Entry(width=14)
input.pack()
# input_string = input.get()









window.mainloop()
