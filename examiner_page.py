import tkinter as tk
from tkinter import messagebox
from database import execute_query, fetch_data  # Ensure fetch_data is defined to retrieve questions

def open_examiner_page():
    examiner_window = tk.Toplevel()
    examiner_window.title("Add or Modify Questions")

    # Labels and Entry fields for adding a new question
    tk.Label(examiner_window, text="Question").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    question_entry = tk.Entry(examiner_window, width=50)
    question_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(examiner_window, text="Option 1").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    option1_entry = tk.Entry(examiner_window, width=50)
    option1_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(examiner_window, text="Option 2").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    option2_entry = tk.Entry(examiner_window, width=50)
    option2_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(examiner_window, text="Option 3").grid(row=3, column=0, padx=10, pady=5, sticky="w")
    option3_entry = tk.Entry(examiner_window, width=50)
    option3_entry.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(examiner_window, text="Option 4").grid(row=4, column=0, padx=10, pady=5, sticky="w")
    option4_entry = tk.Entry(examiner_window, width=50)
    option4_entry.grid(row=4, column=1, padx=10, pady=5)

    tk.Label(examiner_window, text="Correct Answer (1-4)").grid(row=5, column=0, padx=10, pady=5, sticky="w")
    correct_answer_entry = tk.Entry(examiner_window, width=10)
    correct_answer_entry.grid(row=5, column=1, padx=10, pady=5)

    def add_question():
        question = question_entry.get()
        options = [option1_entry.get(), option2_entry.get(), option3_entry.get(), option4_entry.get()]
        correct_answer = correct_answer_entry.get()

        if not question or not all(options) or not correct_answer:
            messagebox.showerror("Error", "All fields are required.")
            return

        try:
            correct_answer = int(correct_answer)
            if correct_answer not in [1, 2, 3, 4]:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Correct answer must be a number between 1 and 4.")
            return

        execute_query("""
            INSERT INTO questions (question_text, option1, option2, option3, option4, correct_answer)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (question, options[0], options[1], options[2], options[3], correct_answer))

        messagebox.showinfo("Success", "Question added successfully.")
        question_entry.delete(0, tk.END)
        option1_entry.delete(0, tk.END)
        option2_entry.delete(0, tk.END)
        option3_entry.delete(0, tk.END)
        option4_entry.delete(0, tk.END)
        correct_answer_entry.delete(0, tk.END)

    submit_button = tk.Button(examiner_window, text="Submit", command=add_question, bg='light blue')
    submit_button.grid(row=6, column=0, columnspan=2, pady=10)

    # Optional Delete Section
    def toggle_delete_section():
        if delete_section_frame.winfo_ismapped():
            delete_section_frame.grid_remove()
        else:
            delete_section_frame.grid()

    # Delete Section
    delete_section_frame = tk.Frame(examiner_window)
    delete_section_frame.grid(row=8, column=0, columnspan=2, padx=10, pady=10)
    delete_section_frame.grid_remove()  # Hide by default

    tk.Label(delete_section_frame, text="Delete Question by ID").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    delete_id_entry = tk.Entry(delete_section_frame, width=10)
    delete_id_entry.grid(row=0, column=1, padx=10, pady=5)

    def delete_question():
        question_id = delete_id_entry.get()

        if not question_id:
            messagebox.showerror("Error", "Question ID is required to delete.")
            return

        try:
            question_id = int(question_id)
        except ValueError:
            messagebox.showerror("Error", "Question ID must be a valid integer.")
            return

        question = fetch_data("SELECT * FROM questions WHERE id=%s", (question_id,))
        if not question:
            messagebox.showerror("Error", "No question found with the specified ID.")
            return

        # Delete associated answers before deleting the question
        execute_query("DELETE FROM answers WHERE question_id=%s", (question_id,))
        execute_query("DELETE FROM questions WHERE id=%s", (question_id,))

        messagebox.showinfo("Success", "Question and associated answers deleted successfully.")
        delete_id_entry.delete(0, tk.END)

    delete_button = tk.Button(delete_section_frame, text="Delete", command=delete_question, bg='yellow')
    delete_button.grid(row=1, column=0, columnspan=2, pady=10)

    # Toggle Button for Delete Section
    toggle_delete_button = tk.Button(examiner_window, text="Delete Question", command=toggle_delete_section)
    toggle_delete_button.grid(row=7, column=0, columnspan=2, pady=5)
