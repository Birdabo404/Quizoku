'''
    Author: Clyde Heinrich "Birdabo" Lontoc
    Details: A python quiz application using Tkinter & Tkkbootstrap libray as the main GUI toolkit.
    Date: May 1st 2025
'''

import tkinter
from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap import Style, Entry, Button, Label
from tkinter import messagebox, filedialog
import csv
import datetime
import os

def quiz_sheet_Reader():
    Quizsheet = []
    try:
        with open("Quizsheet.csv", "r") as file:
            reader = csv.DictReader(file) 
            for row in reader:
                question = {  
                    "type": row["type"],
                    "text": row["question"],
                }
                
                # Handle different question types
                if row["type"] == "MCQ":
                    question["options"] = [
                        row["option1"],
                        row["option2"],
                        row["option3"],
                        row["option4"]
                    ]
                    question["answer"] = row["answer"]
                elif row["type"] == "Fill":
                    question["answer"] = row["answer"]
                elif row["type"] == "TrueFalse":
                    question["answer"] = row["answer"]
                
                Quizsheet.append(question)
        return Quizsheet
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load quiz questions: {e}")
        return []

def on_Submit():
    student_Name = name_entry.get()
    student_Id = id_entry.get()
    
    if not student_Name or not student_Id:
        messagebox.showwarning("Warning", "Please enter both your name and ID")
        return
        
    print(f"Student Name: {student_Name}, student ID: {student_Id}")

    answer = messagebox.askquestion("Question", "Continue with the Questions?")
    if answer == "yes":
        root.withdraw()
        start_Quiz(student_Name, student_Id)
    else:
        messagebox.showinfo("Result", "You disagreed. Exiting...")
        root.deiconify()

def start_Quiz(student_Name, student_Id):
    quiz_window = ttk.Toplevel()
    quiz_window.title(f"Quizoku Running - {student_Name} - {student_Id}")
    quiz_window.geometry('620x420')
    questions = quiz_sheet_Reader()
    current_question = 0
    score = 0
    
    user_responses = []
    
    # Variables to store user answers
    user_answer = tkinter.StringVar()
    entry_var = tkinter.StringVar()

    def show_question():
        # Clear previous widgets to make new 
        for widget in quiz_window.winfo_children():
            widget.destroy()
        
        # Progress indicator
        progress_label = ttk.Label(quiz_window, 
                                  text=f"Question {current_question + 1} of {len(questions)}")
        progress_label.pack(pady=5)
        
        # Get current question
        q = questions[current_question]
        
        # Question text
        question_label = ttk.Label(quiz_window, text=q["text"], font=("Helvetica", 14))
        question_label.pack(pady=10)
        
        # Reset variables
        user_answer.set("")
        entry_var.set("")
        
        if q["type"] == "MCQ":
            answer_frame = ttk.Frame(quiz_window)
            answer_frame.pack(pady=10)
            
            for option in q["options"]:
                ttk.Radiobutton(answer_frame, 
                               text=option, 
                               value=option, 
                               variable=user_answer).pack(anchor="w", pady=5)
                
        elif q["type"] == "Fill":
            ttk.Label(quiz_window, text="Your Answer:").pack()
            ttk.Entry(quiz_window, textvariable=entry_var).pack(pady=10)
            
        else:  # True/False
            tf_frame = ttk.Frame(quiz_window)
            tf_frame.pack(pady=10)
            
            ttk.Radiobutton(tf_frame, text="True", value="True", variable=user_answer).pack(side=LEFT, padx=10)
            ttk.Radiobutton(tf_frame, text="False", value="False", variable=user_answer).pack(side=LEFT, padx=10)
        
        # Submit Button
        ttk.Button(quiz_window, text="Submit Answer", command=check_answer, bootstyle="primary").pack(pady=20)

    def check_answer():
        nonlocal current_question, score
        q = questions[current_question]
        correct = False
        selected = ""
        
        if q["type"] == "MCQ" or q["type"] == "TrueFalse":
            selected = user_answer.get()
            if selected == q["answer"]:
                correct = True
        elif q["type"] == "Fill":
            selected = entry_var.get().strip().lower()
            correct_answer = q["answer"].lower()
            if selected == correct_answer:
                correct = True
        
        user_responses.append({
            "question": q["text"],
            "user_answer": selected,
            "correct_answer": q["answer"],
            "is_correct": correct
        })
        
        # Show feedback
        if correct:
            score += 1
            messagebox.showinfo("Correct!", "Your answer is correct! ✅")
        else:
            messagebox.showinfo("Incorrect", f"Incorrect ❌ The answer is: {q['answer']}")
        
        # Move to next question
        current_question += 1
        
        if current_question < len(questions):
            show_question()  # Next question
        else:
            show_results()  # End quiz

    def save_results():
        # Create filename with date, name and ID
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        filename = f"{current_date}_{student_Name}_{student_Id}_results.txt"
        
        # Remove any invalid characters from filename
        filename = "".join(c for c in filename if c.isalnum() or c in ['_', '-', '.'])
        
        try:
            # Ensure the Results directory exists
            if not os.path.exists("Results"):
                os.makedirs("Results")
                
            # Full path for the results file
            file_path = os.path.join("Results", filename)
            
            # Write results to file
            with open(file_path, "w") as file:
                file.write(f"Quiz Results\n")
                file.write(f"===========\n\n")
                file.write(f"Date: {current_date}\n")
                file.write(f"Student Name: {student_Name}\n")
                file.write(f"Student ID: {student_Id}\n\n")
                file.write(f"Score: {score}/{len(questions)}\n")
                file.write(f"Percentage: {int((score/len(questions))*100)}%\n\n")
                
                # Add details about each question and the user's responses
                file.write("Question Details:\n")
                file.write("================\n\n")
                
                for i, response in enumerate(user_responses):
                    file.write(f"{i+1}. {response['question']}\n")
                    file.write(f"   Your Answer: {response['user_answer']}\n")
                    file.write(f"   Correct Answer: {response['correct_answer']}\n")
                    file.write(f"   Result: {'✓ Correct' if response['is_correct'] else '✗ Incorrect'}\n\n")
            
            messagebox.showinfo("Success", f"Results saved to:\n{file_path}")
            return True
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save results: {e}")
            return False
            
    def show_results():
        for widget in quiz_window.winfo_children():
            widget.destroy()
            
        result_frame = ttk.Frame(quiz_window)
        result_frame.pack(expand=True)
        
        ttk.Label(result_frame, 
                 text=f"Quiz Complete!", 
                 font=("Helvetica", 18, "bold")).pack(pady=10)
        
        ttk.Label(result_frame, 
                 text=f"Student: {student_Name}", 
                 font=("Helvetica", 12)).pack(pady=5)
                 
        ttk.Label(result_frame, 
                 text=f"ID: {student_Id}", 
                 font=("Helvetica", 12)).pack(pady=5)
        
        final_score = ttk.Label(result_frame, 
                              text=f"Your score: {score}/{len(questions)} ({int((score/len(questions))*100)}%)",
                              font=("Helvetica", 14))
        final_score.pack(pady=20)
        
        # Add button to save results
        ttk.Button(result_frame,
                  text="Save Results",
                  command=save_results,
                  bootstyle="success").pack(pady=10)
        
        ttk.Button(result_frame, 
                  text="Exit", 
                  command=lambda: [quiz_window.destroy(), root.deiconify()], 
                  bootstyle="danger").pack(pady=10)

    if questions:
        show_question()  # Start with first question
    else:
        messagebox.showerror("Error", "No questions loaded. Exiting quiz.")
        quiz_window.destroy()
        root.deiconify()
    
    quiz_window.protocol("WM_DELETE_WINDOW", lambda: [quiz_window.destroy(), root.deiconify()])

def button_Quit():
    root.destroy()

# Main window - welcome UI
root = tkinter.Tk()

Style = Style(theme='vapor')
root.title("Quizoku - Welcome")
root.geometry('620x420')

welcome_Label = ttk.Label(root, text='Welcome Student!', font=('Helvetica', 20, 'bold'))
welcome_Label.pack(pady=50)

# Taking student name
name_label = ttk.Label(root, text="Student Name:")
name_label.pack()
name_entry = ttk.Entry(root, bootstyle="primary")
name_entry.pack(pady=10)

# Taking Student ID num
id_label = ttk.Label(root, text="ID Number:")
id_label.pack()
id_entry = ttk.Entry(root, bootstyle="primary")
id_entry.pack()

# Button submission 1st Page
button_submit = ttk.Button(root, text='Submit', bootstyle="success")
button_submit.pack(pady=10)
button_submit.config(command=on_Submit)

button_exit = ttk.Button(root, text='Exit', bootstyle="danger", width=5)
button_exit.pack()
button_exit.config(command=button_Quit)

root.mainloop()