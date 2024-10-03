# Task 3 - Password Generator using Tkinter
# A unique GUI-based password generator application

import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate a random password
def generate_password():
    # Retrieve the desired password length from the input field
    password_length = int(entry_password_length.get())

    # Check if the length is at least 8 characters
    if password_length < 8:
        messagebox.showwarning("Warning", "Password length should be at least 8 characters.")
        return

    # Define character sets for the password (letters, digits, and punctuation)
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password by randomly selecting characters from the defined set
    generated_password = ''.join(random.choice(characters) for _ in range(password_length))

    # Display the generated password in the entry field
    entry_generated_password.delete(0, tk.END)  # Clear the entry field
    entry_generated_password.insert(tk.END, generated_password)  # Insert the new password

# Function to reset the input fields
def reset_fields():
    # Clear all entry fields to allow for new input
    entry_username.delete(0, tk.END)
    entry_password_length.delete(0, tk.END)
    entry_generated_password.delete(0, tk.END)

# Main function to set up the GUI
def main():
    global entry_username, entry_password_length, entry_generated_password
    root = tk.Tk()  # Create the main window
    root.title("Unique Password Generator")  # Set the window title

    # Create and position GUI components
    tk.Label(root, text="Password Generator", font=("Helvetica", 16, "bold")).grid(row=0, column=0, columnspan=3, pady=20)

    tk.Label(root, text="Enter Username:").grid(row=1, column=0, sticky=tk.E)  # Label for username
    entry_username = tk.Entry(root, width=30)  # Input field for username
    entry_username.grid(row=1, column=1, columnspan=2)

    tk.Label(root, text="Enter Password Length:").grid(row=2, column=0, sticky=tk.E)  # Label for password length
    entry_password_length = tk.Entry(root, width=10)  # Input field for password length
    entry_password_length.grid(row=2, column=1)

    tk.Label(root, text="Generated Password:").grid(row=3, column=0, sticky=tk.E)  # Label for generated password
    entry_generated_password = tk.Entry(root, width=30)  # Input field for displaying generated password
    entry_generated_password.grid(row=3, column=1, columnspan=2)

    # Create buttons with colors and associate them with their respective functions
    tk.Button(root, text="Generate Password", command=generate_password, bg='lightgreen', fg='black').grid(row=4, column=0, padx=5, pady=10)
    tk.Button(root, text="Reset", command=reset_fields, bg='lightcoral', fg='black').grid(row=4, column=1, padx=5, pady=10)

    root.mainloop()  # Start the GUI event loop

# Entry point of the program
if __name__ == "__main__":
    main()
