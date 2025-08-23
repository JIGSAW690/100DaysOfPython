from tkinter import *

def calculate():
    distance_in_miles = float(input.get())
    distance_in_km = distance_in_miles * 1.60934
    kilo_label.config(text=distance_in_km)

#Creating the App Screen
window = Tk()
window.minsize(width=250, height=250)
window.title('Miles to Kilometers converter')

#Creating the Entry for user input
input = Entry(window)
input.grid(column=1, row=0)

#Creating the label for Miles Unit
miles = Label(window, text='Miles')
miles.grid(column=2, row=0)
miles.config(padx=20, pady=20)

#Creating Label for sentence
label = Label(window, text='is equal to: ')
label.grid(column=0, row=1)

#Creating Label for result in Km
kilo_label = Label(window)
kilo_label.grid(column=1, row=1)

#Creating the label for Km Unit
kilo = Label(window, text='Kilometers')
kilo.grid(column=2, row=1)
kilo.config(padx=20, pady=20)

#Creating the calculate button
cal = Button(window, text='Calculate', command=calculate)
cal.grid(column=1, row=2)

#Creating the close button
close = Button(window, text='Close', command=window.destroy)
close.grid(column=2, row=2)

window.mainloop()

