import tkinter as tk
from tkinter import messagebox
from database import fetch_data, execute_query

def open_quiz_page(user_id):
    quiz_window = tk.Toplevel()
    quiz_window.title("Quiz Page")

    question_label = tk.Label(quiz_window, text="")
    question_label.pack()

    answer_var = tk.StringVar()
    options = [tk.Radiobutton(quiz_window, variable=answer_var, value=str(i)) for i in range(4)]
    for option in options:
        option.pack(anchor="w")

    # Fetch all questions once
    questions = fetch_data(
        "SELECT id, question_text, option1, option2, option3, option4, correct_answer FROM questions"
    )
    
    # Variable to track the current question index and score
    current_question_index = [0]  # Start with the first question in the list
    score = [0]  # Mutable score variable to keep track of the participant's score

    def load_question():
        if current_question_index[0] < len(questions):
            question_data = questions[current_question_index[0]]
            question_label.config(text=question_data[1])
            for i, option in enumerate(options):
                option.config(text=question_data[i + 2], value=str(i + 1))
            answer_var.set("")  # Reset the answer selection
        else:
            # If there are no more questions, show the score and close the window
            messagebox.showinfo("Quiz Completed", f"Your score is: {score[0]}")
            quiz_window.destroy()

    def submit_answer():
        selected_answer = answer_var.get()
        if selected_answer:
            correct_answer = questions[current_question_index[0]][6]  # Get the correct answer

            # Check if the answer is correct and update score
            if selected_answer == str(correct_answer):
                score[0] += 1

            execute_query(
                "INSERT INTO answers (user_id, question_id, answer) VALUES (%s, %s, %s)",
                (user_id, questions[current_question_index[0]][0], selected_answer)
            )
            messagebox.showinfo("Quiz", "Answer Submitted")
            current_question_index[0] += 1  # Move to the next question
            load_question()  # Load the next question
        else:
            messagebox.showerror("Error", "Please select an answer before submitting.")

    # Load the first question
    load_question()

    # Button to submit the answer
    tk.Button(quiz_window, text="Submit Answer", command=submit_answer).pack()
