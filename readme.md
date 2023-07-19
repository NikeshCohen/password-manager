# Password Manager

A simple password manager that allows you to store your website passwords offline and in a secure way.

Update v1.2: Changed data file to json format. Added a search feature which will return the account information. Added more try and except tests to ensure there are no errors when running the program

Future Updates: Improving the UI

## Features

- Generate strong passwords
- Save passwords to a text file
- Copy the generated password to the clipboard automatically

## Usage

1. Change the default email address in line 134 to your own for ease of use `email_input.insert(0, "me@email.com")`
2. Run the program using the following command: python main.py
3. Enter the website name, email address, and password.
4. Click the "Generate password" button to generate a strong password or use your own password.
5. Click the "Add" button to save the password.

## Requirements

- Python 3
- The `tkinter` module
- The `pyperclip` module(install the module with the following command: pip install pyperclip)
