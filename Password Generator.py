import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

# Function to generate password
def generate_password():
    length = int(length_entry.get())

    lower = string.ascii_lowercase if lower_var.get() else ""
    upper = string.ascii_uppercase if upper_var.get() else ""
    digits = string.digits if digits_var.get() else ""
    special = string.punctuation if special_var.get() else ""

    # Check if at least one character set is selected
    if not (lower or upper or digits or special):
        messagebox.showwarning("Selection Error", "Please select at least one character set.")
        return

    all_chars = lower + upper + digits + special
    password = ''.join(random.choice(all_chars) for _ in range(length))

    # Enforce security rules if all character sets are selected
    if lower and upper and digits and special:
        while not (any(c.islower() for c in password) and any(c.isupper() for c in password) and
                   any(c.isdigit() for c in password) and any(c in string.punctuation for c in password)):
            password = ''.join(random.choice(all_chars) for _ in range(length))

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Function to copy password to clipboard
def copy_to_clipboard():
    pyperclip.copy(password_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Function to validate user input for length
def validate_length(P):
    if P.isdigit() and 8 <= int(P) <= 32:
        return True
    elif P == "":
        return True
    else:
        return False

# Function to show about information
def show_about():
    about_text = (
        "This is an Advanced Password Generator to generate strong and secure passwords.\n"
        "Functions:\n"
        "1. Randomization: Generate random passwords using selected character sets.\n"
        "2. User Input Validation: Validate password length to ensure it's between 8 and 32 characters.\n"
        "3. Character Set Handling: Manage different character sets (letters, numbers, symbols).\n"
        "4. GUI Design: Create an intuitive and user-friendly interface for password generation.\n"
        "5. Security Rules: Implement rules for generating strong, secure passwords.\n"
        "6. Clipboard Integration: Copy generated passwords to the clipboard for convenience.\n"
        "7. Customization: Enable users to customize password generation further.\n\n\n"
        "Created By Anurag Kumar\nUsing Python and Tkinter"
    )
    messagebox.showinfo("About", about_text)

root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("400x400")
root.configure(bg="#87CEEB")

# Create Menu Bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="About", menu=help_menu)
help_menu.add_command(label="About", command=show_about)

# Length Frame
length_frame = tk.Frame(root, bg="#87CEEB")
length_frame.pack(pady=20)
length_label = tk.Label(length_frame, text="Password Length (8-32):", bg="#87CEEB", fg="#333333", font=("Helvetica", 12))
length_label.pack(side=tk.LEFT)
length_entry = tk.Entry(length_frame, validate="key", validatecommand=(root.register(validate_length), "%P"), width=5, font=("Helvetica", 12))
length_entry.pack(side=tk.LEFT)

# Options Frame
options_frame = tk.Frame(root, bg="#87CEEB")
options_frame.pack(pady=20)
lower_var = tk.BooleanVar()
upper_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
special_var = tk.BooleanVar()
lower_check = tk.Checkbutton(options_frame, text="Lowercase (a-z)", variable=lower_var, bg="#87CEEB", fg="#333333", font=("Helvetica", 12))
upper_check = tk.Checkbutton(options_frame, text="Uppercase (A-Z)", variable=upper_var, bg="#87CEEB", fg="#333333", font=("Helvetica", 12))
digits_check = tk.Checkbutton(options_frame, text="Digits (0-9)", variable=digits_var, bg="#87CEEB", fg="#333333", font=("Helvetica", 12))
special_check = tk.Checkbutton(options_frame, text="Special Characters (!@#$%^&*)", variable=special_var, bg="#87CEEB", fg="#333333", font=("Helvetica", 12))
lower_check.pack(anchor=tk.W)
upper_check.pack(anchor=tk.W)
digits_check.pack(anchor=tk.W)
special_check.pack(anchor=tk.W)

# Generate Button
generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg="#4caf50", fg="#ffffff", font=("Helvetica", 12))
generate_button.pack(pady=20)

# Password Entry
password_entry = tk.Entry(root, width=30, font=("Helvetica", 12))
password_entry.pack(pady=10)

# Copy Button
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg="#2196f3", fg="#ffffff", font=("Helvetica", 12))
copy_button.pack(pady=10)

root.mainloop()
