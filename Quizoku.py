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



root = tkinter.Tk()
Style = Style(theme = 'cosmo')
root.title("Quizoku - Welcome")
root.geometry('620x420')

welcome_Label = ttk.Label(root, text='Welcome Student!', font=('Helvetica, 20'))
welcome_Label.pack(pady=50)

name_label = ttk.Label(text="Student Name:")
name_label.pack()
name_entry = ttk.Entry(bootstyle="primary")
name_entry.pack(pady=10)
id_label = ttk.Label(text="ID Number:")
id_label.pack()
id_entry = ttk.Entry(bootstyle="primary")
id_entry.pack()
id_submit = ttk.Button(text='Submit', bootstyle="success", )
id_submit.pack(pady=10)

root.mainloop()