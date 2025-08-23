from tkinter import *
from tkinter import messagebox
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    password_list += [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)
    pass_string = ''.join(password_list)
    blank_password_entry.insert(0, pass_string)
    #print(pass_string)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def reset_fields():
    blank_email_entry.delete(0, END)
    blank_email_entry.insert(0, "<EMAIL>")
    blank_password_entry.delete(0, END)
    blank_web_entry.delete(0, END)

def save_password():
    if blank_web_entry.get() == "" or blank_email_entry.get() == "" or blank_password_entry.get() == "":
        messagebox.showerror("Error", "Please fill all fields")
    elif not blank_email_entry.get().endswith('.com'):
        messagebox.showerror("Error", "Please enter a valid email")
    else:
        is_ok = messagebox.askyesno("Credentials", f"Email Entered: {blank_email_entry.get()}\n"
                                           f"Password Entered: {blank_password_entry.get()}\n"
                                           f"Is it okay to save these credentials?")
        if is_ok:
            with open('data.txt', 'a') as file:
                file.write(f"{blank_web_entry.get()}\t|\t{blank_email_entry.get()}\t|\t{blank_password_entry.get()}\n")
            messagebox.showinfo("Success", "Password has been saved successfully")
            reset_fields()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(window, width=200, height=200)
image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

#Labels
web_label = Label(window, text="Website: ")
web_label.grid(row=1, column=0)

email_label = Label(window, text="Email/Username: ")
email_label.grid(row=2, column=0)

password_label = Label(window, text="Password: ")
password_label.grid(row=3, column=0)

#Entries
blank_web_entry = Entry(window, width=35)
blank_web_entry.grid(row=1, column=1, columnspan=2)
blank_web_entry.focus()

blank_email_entry = Entry(window, width=35)
blank_email_entry.grid(row=2, column=1, columnspan=2)
blank_email_entry.insert(0, "<EMAIL>")

blank_password_entry = Entry(window, width=17)
blank_password_entry.grid(row=3, column=1)

#Buttons
generate_button = Button(text='Generate Password', command=generate_password)
generate_button.grid(row=3, column=2, ipady=2, sticky='ns')

add_button = Button(text='Add', width=29, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)






window.mainloop()
