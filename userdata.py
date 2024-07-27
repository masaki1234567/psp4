import tkinter as tk
from tkinter import messagebox
import csv
import os

class UserInfoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("User Information")

        # Username label and entry
        self.username_label = tk.Label(root, text="Username:")
        self.username_label.grid(row=0, column=0, padx=10, pady=10)
        self.username_entry = tk.Entry(root)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        # Email label and entry
        self.email_label = tk.Label(root, text="Email:")
        self.email_label.grid(row=1, column=0, padx=10, pady=10)
        self.email_entry = tk.Entry(root)
        self.email_entry.grid(row=1, column=1, padx=10, pady=10)

        # Save button
        self.save_button = tk.Button(root, text="Save", command=self.save_info)
        self.save_button.grid(row=2, columnspan=2, pady=10)

    def save_info(self):
        username = self.username_entry.get()
        email = self.email_entry.get()

        if not username or not email:
            messagebox.showwarning("Input Error", "Please enter both username and email.")
            return

        file_exists = os.path.isfile("userdata.csv")

        with open("userdata.csv", "a", newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["Username", "Email"])
            writer.writerow([username, email])

        messagebox.showinfo("Success", "Information saved successfully!")
        self.username_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = UserInfoApp(root)
    root.mainloop()
