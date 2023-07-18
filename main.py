import tkinter as tk
from pyperclip import copy
from random import choice, randint, shuffle
from tkinter import messagebox


# ---------------------------- Functions------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(
            title="Invalid input", message="Please do not leave any fields empty"
        )
    else:
        save = messagebox.askokcancel(
            title=website,
            message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\nWould you like to save this information?",
        )

        if save:
            with open("data.txt", "a") as data_file:
                data_file.write("\n------------------------------------")
                data_file.write(f"\n{website} | {email} | {password}\n")

                website_input.delete(0, tk.END)
                password_input.delete(0, tk.END)


def password_gen():
    password_input.delete(0, tk.END)

    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password_letters = [choice(letters) for _ in range(randint(6, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)
    copy(password)


# ---------------------------- UI SETUP ------------------------------- #

# Window
window = tk.Tk()
window.resizable(False, False)
window.config(padx=20, pady=20)
window.title("Password manager")

# Image canvas
canvas = tk.Canvas(width=200, height=200)
lock_image = tk.PhotoImage(file="images/logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)


# Website input
website_label = tk.Label(text="Website:")
website_label.grid(row=1, column=0)

website_input = tk.Entry()
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2, sticky="EW", pady=3)


# Username input
email_label = tk.Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_input = tk.Entry()
email_input.insert(0, "me@email.com")
email_input.grid(row=2, column=1, columnspan=2, sticky="EW", pady=3)


# Password input
password_label = tk.Label(text="Password:")
password_label.grid(row=3, column=0, sticky="EW", pady=3)

password_input = tk.Entry(width=21)
password_input.grid(row=3, column=1, sticky="EW", pady=3)


# Button

# # Password generation button
password_gen_button = tk.Button(text="Generate password", command=password_gen)
password_gen_button.grid(row=3, column=2, sticky="EW", pady=3, padx=(10, 0))

# # Add button
add_button = tk.Button(text="Add", width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW", pady=3)


window.mainloop()
