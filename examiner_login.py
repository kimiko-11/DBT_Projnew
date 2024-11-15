import tkinter as tk
from tkinter import messagebox
from database import fetch_data
from examiner_page import open_examiner_page

def examiner_login():
    def login():
        username = username_entry.get()
        password = password_entry.get()

        # Query for login
        user = fetch_data("SELECT * FROM staff WHERE username=%s AND spassword=%s", (username, password))
        if user:
            messagebox.showinfo("Login", "Login Successful")
            login_window.destroy()  # Close the login window after successful login
            open_examiner_page()  # Open examiner question management page
        else:
            messagebox.showerror("Login", "Invalid Credentials")

    # GUI for examiner login page
    login_window = tk.Tk()
    login_window.title("Examiner Login")

    tk.Label(login_window, text="Username").pack()
    username_entry = tk.Entry(login_window)
    username_entry.pack()

    tk.Label(login_window, text="Password").pack()
    password_entry = tk.Entry(login_window, show="*")
    password_entry.pack()

    tk.Button(login_window, text="Login", command=login,bg='light blue').pack()
    login_window.mainloop()
