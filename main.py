from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

import random

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    password_letters = [random.choice(letters) for char in range(nr_letters)]

    password_symbol = [random.choice(symbols) for char in range(nr_symbols)]

    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = password_symbol + password_letters + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_information():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "email" : email,
            "password" : password
        }
    }
    if len(password) == 0  or len(website) == 0:
        messagebox.showinfo(title="Oops", message="Please do not leave any fields empty!")
    else:
        try:
            with open("data.json", mode="r") as data_file:
            # Reading the old data
                data = json.load(data_file)
            # Updating old data with New data
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", mode="w") as data_file:
                # saving the updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

def find_password():
        website = website_entry.get()
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Oops", message="The input does not exist")
        else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=f"{website}", message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(title="error", message="The input does not exist")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="website:")
website_label.grid(column=0, row=1)
email_label = Label(text="email/username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=40)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan= 2)
email_entry = Entry(width=40)
email_entry.insert(0, "yuvigulati007@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width= 21)
password_entry.grid(column=1, row=3)

# Buttons
generate_button = Button(text="Generate Password",command= generate_password)
generate_button.grid(column=2,row=3)
add_button = Button(text="Add", width=36, command=save_information)
add_button.grid(column=1, row=4, columnspan=2)
search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1)


window.mainloop()