from tkinter import *

window = Tk()
label = Label(window,text = 'Welcome to Tkinter')
button = Button(window, text = 'Click Me')
label.pack()
button.pack()

window.mainloop()