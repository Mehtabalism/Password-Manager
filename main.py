from tkinter import *
from tkinter import messagebox
import random
import json
WHITE = "#FFFFFF"

# ---------------------------- JSON File Location ------------------------------- #
file_location = "D:/Pycharm Projects/Password_Manager.json"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    password_list = [random.choice(letters) for char in range(random.randint(8, 10))] + \
                    [random.choice(symbols) for char in range(random.randint(2, 4))] + \
                    [random.choice(numbers) for char in range(random.randint(2, 4))]
    random.shuffle(password_list)
    password = "".join(password_list)

    entry_password.delete(0, END)
    entry_password.insert(0, password)
    window.clipboard_clear()
    window.clipboard_append(password)
# ---------------------------- Search ------------------------------- #
def search():
    try:
        with open(file_location, mode="r") as file:
            data = json.load(file)
            old_password = data[entry_website.get()]["password"]
    except FileNotFoundError:
        messagebox.showerror(message="No Data File Found.")
    except KeyError:
        messagebox.showinfo(title=entry_website.get(), message=f"There is no account registered for {entry_website.get()}.")
    else:
        messagebox.showinfo(title=entry_website.get(), message=f"Email: {entry_username.get()}\n"
                                                               f"Password: {old_password}")
        window.clipboard_append(old_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    new_data = {
        entry_website.get(): {
            "email": entry_username.get(),
            "password": entry_password.get()
        }
    }
    if len(entry_website.get()) == 0 or len(entry_username.get()) == 0 or len(entry_password.get()) == 0:
        messagebox.showinfo(message="Please fill in all fields!")
    else:
        try:
            with open(file_location, mode="r") as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            with open(file_location, mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            with open(file_location, mode="w") as file:
                json.dump(data, file, indent=4)
        entry_website.delete(0, END)
        entry_password.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg=WHITE)

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:", bg=WHITE, width=13, anchor="e")
label_website.grid(column=0, row=1)
label_username = Label(text="Email/Username:", bg=WHITE, width=13, anchor="e")
label_username.grid(column=0, row=2)
label_password = Label(text="Password:", bg=WHITE, width=13, anchor="e")
label_password.grid(column=0, row=3)

entry_website = Entry(bd=2)
entry_website.grid(column=1, row=1, columnspan=1, sticky="EW")
entry_username = Entry(bd=2)
entry_username.grid(column=1, row=2, columnspan=2, sticky="EW")
entry_password = Entry(bd=2)
entry_password.grid(column=1, row=3, sticky="EW")

button_search = Button(text="Search", command=search)
button_search.grid(column=2, row=1, padx=2, pady=2, sticky="EW")
button_generate_password = Button(text="Generate Password", command=generate_password)
button_generate_password.grid(column=2, row=3, padx=2, pady=2, sticky="EW")
button_add = Button(text="Add", command=save)
button_add.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
