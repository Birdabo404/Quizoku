import tkinter
from tkinter import ttk

import sv_ttk

root = tkinter.Tk()

def toggle_theme():
    if sv_ttk.get_theme() == "dark":
        print("Setting theme to light")
        sv_ttk.use_light_theme()
    elif sv_ttk.get_theme() == "light":
        print("Setting theme to dark")
        sv_ttk.use_dark_theme()
    else:
        print("Not Sun Valley theme")

button = ttk.Button(root, text="Toggle theme", command=toggle_theme)
button.pack()

root.mainloop()