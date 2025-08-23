from tkinter import *

window = Tk()
window.minsize(width=800, height=600)
window.title('Tkinter Widgets placed using GRID Placement')
window.config(padx=50, pady=50)

label = Label(window, text='This is a sample label which will be placed using grid')
label.grid(column=0, row=0)

submit = Button(window, text='SUBMIT', width=10, command=window.destroy)
submit.grid(column=1, row=1)

reset = Button(window, text='RESET', width=10)
reset.grid(column=2, row=0)

input = Entry(window)
input.grid(column=3, row=2)
window.mainloop()
