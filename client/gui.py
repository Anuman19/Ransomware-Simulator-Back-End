import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

import encryptor as encryptor  # Ensure that 'encryptor' is a module in the same directory or installed


def create_file(file_name):
    """
    Creates a file with dummy data for testing encryption functionality.

    :param file_name: Name of the file to create.
    :return: The name of the created file.
    """
    try:
        with open(file_name, 'x') as demoFile:
            demoFile.write(
                "This file was created to test the encryption functionality with dummy data.\n"
                "Bank-Login:\tadmin\nPW:\t\tCashMoney1"
            )
            messagebox.showinfo("File Created", "File created successfully.")
            return file_name
    except FileExistsError:
        messagebox.showwarning("File Exists", "File already exists, removing existing file and creating a new one.")
        os.remove(file_name)
        return create_file(file_name)


def encrypt_file():
    file = filedialog.askopenfilename()
    if file:
        encryptor.file_encrypt(file)
        messagebox.showinfo("Encryption Complete", "File encrypted successfully.")


def decrypt_file():
    file = filedialog.askopenfilename()
    if file:
        encryptor.file_decrypt(file)
        messagebox.showinfo("Decryption Complete", "File decrypted successfully.")


# Create the main window
root = tk.Tk()
root.title("File Encryption/Decryption")

# Create buttons
encrypt_button = tk.Button(root, text="Encrypt File", command=encrypt_file)
encrypt_button.pack(pady=10)

decrypt_button = tk.Button(root, text="Decrypt File", command=decrypt_file)
decrypt_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
