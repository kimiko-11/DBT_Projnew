import tkinter as tk
from tkinter import messagebox
from database import fetch_data

def open_leaderboard():
    leaderboard_window = tk.Toplevel()
    leaderboard_window.title("Leaderboard")

    leaderboard_label = tk.Label(leaderboard_window, text="Leaderboard", font=("Helvetica", 16))
    leaderboard_label.pack()

    leaderboard_frame = tk.Frame(leaderboard_window)
    leaderboard_frame.pack()

    # Fetch leaderboard data from the database
    leaderboard_data = fetch_data("""
        SELECT u.username, IFNULL(SUM(a.is_correct), 0) AS score
        FROM users u
        LEFT JOIN answers a ON u.id = a.user_id
        GROUP BY u.username
        ORDER BY score DESC
    """)

    if leaderboard_data:
        # Display the leaderboard in a table format
        for i, (username, score) in enumerate(leaderboard_data, start=1):
            rank_label = tk.Label(leaderboard_frame, text=f"{i}. {username} - {score} points", font=("Helvetica", 12))
            rank_label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
    else:
        messagebox.showinfo("Leaderboard", "No scores available yet.")

    tk.Button(leaderboard_window, text="Close", command=leaderboard_window.destroy).pack()

    leaderboard_window.mainloop()
