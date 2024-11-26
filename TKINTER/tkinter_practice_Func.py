#!/bin/python3
"""
"""

import tkinter as tk

class MyGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Practical Section - Tkinter")
        self.root.geometry("600x400")

        self.newLabel = tk.Label(self.root, text="Welcome to Tkinter Practical Section", font=("Arial", 16))
        self.newLabel.pack(padx=20, pady=20)

        self.textBox = tk.Text(self.root, height=3, font=("Arial", 16))
        self.textBox.pack()

        self.button = tk.Button(self.root, text="Submit", font=("Arial", 16), command=self.showmsg)
        self.button.pack(padx=20, pady=20)

        self.root.mainloop()

    def showmsg(self):
        """
        """
        if self.textBox.get("1.0", tk.END).strip() != "":
            self.newLabel2 = tk.Label(self.root, text=f'Hello, {self.textBox.get("1.0", tk.END).strip()}! Welcome', font=("Arial", 16))
            self.newLabel2.pack(padx=20, pady=20)
            print(f'Hello, {self.textBox.get("1.0", tk.END).strip()}! Welcome')
        else:
            self.newLabel2 = tk.Label(self.root, text=f'Hello, Guest! Welcome', font=("Arial", 16))
            self.newLabel2.pack(padx=20, pady=20)
            print(f'Hello, Guest! Welcome')

mygui = MyGUI()