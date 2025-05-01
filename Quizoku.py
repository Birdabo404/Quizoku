'''
    Author: Clyde Heinrich "Birdabo" Lontoc
    Details: A python quiz application using Tkinter & Tkkbootstrap libray as the main GUI toolkit.
    Date: May 1st 2025


    //will add more once finish
'''

import tkinter
from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap import Style, Entry, Button, Label
from tkinter import messagebox

def start_Quiz(student_Name, student_Id):
    # Create a new window for the quiz
    quiz_window = ttk.Toplevel()
    quiz_window.title(f"Quizoku - {student_Name} (ID: {student_Id})")
    
    # Destroy the welcome window (optional)
    root.withdraw()  # Hides the welcome window
    
    # Example quiz widget
    question_label = ttk.Label(quiz_window, text="Sample Question")
    question_label.pack()
    
    # Return to welcome window when quiz closes
    quiz_window.protocol("WM_DELETE_WINDOW", lambda: [quiz_window.destroy(), root.deiconify()])


def on_Submit():
    student_Name = name_entry.get()
    student_Id = id_entry.get()
    print(f"Student Name: {student_Name}, student ID: {student_Id}")

    answer = messagebox.askquestion("Question", "Continue with the Questions?")
    if answer == "yes":
        messagebox.showinfo("Result", "You agreed. Continuing...")
    else:
         messagebox.showinfo("Result", "You disagreed. Exiting...")

root = tkinter.Tk()

Style = Style(theme = 'cosmo')
root.title("Quizoku - Welcome")
root.geometry('620x420')

welcome_Label = ttk.Label(root, text='Welcome Student!', font=('Helvetica, 20'))
welcome_Label.pack(pady=50)

#taking student name
name_label = ttk.Label(text="Student Name:")
name_label.pack()
name_entry = ttk.Entry(bootstyle="primary")
name_entry.pack(pady=10)

#taking Student ID num
id_label = ttk.Label(text="ID Number:")
id_label.pack()
id_entry = ttk.Entry(bootstyle="primary")
id_entry.pack()

# button submition 1st Page
button_submit = ttk.Button(text='Submit', bootstyle="success", )
button_submit.pack(pady=10)
button_submit.config(command=on_Submit)

root.mainloop()