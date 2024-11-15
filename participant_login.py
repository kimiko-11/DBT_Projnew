import tkinter as tk
from tkinter import messagebox
from database import fetch_data
from quiz_page import open_quiz_page  # Import the show_quiz function to call after login

def participant_login():
    def login():
        username = username_entry.get()
        password = password_entry.get()

        # Query updated to match the new column name 'upassword'
        user = fetch_data("SELECT * FROM users WHERE username=%s AND upassword=%s", (username, password))
        if user:
            messagebox.showinfo("Login", "Login Successful")
            login_window.destroy()  # Close the login window
            open_quiz_page(1)  # Show the quiz page
        else:
            messagebox.showerror("Login", "Invalid Credentials")

    # GUI code for participant login page
    login_window = tk.Tk()
    login_window.title("Participant Login")

    tk.Label(login_window, text="Username").pack()
    username_entry = tk.Entry(login_window)
    username_entry.pack()

    tk.Label(login_window, text="Password").pack()
    password_entry = tk.Entry(login_window, show="*")
    password_entry.pack()

    tk.Button(login_window, text="Login", command=login,bg='light blue').pack()
    login_window.mainloop()
