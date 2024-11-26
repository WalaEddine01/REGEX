#!/bin/python3
"""
"""

import tkinter as tk

root = tk.Tk()
root.title("Practical Section - Tkinter")

root.geometry("600x400")
newLabel = tk.Label(root, text="Welcome to Tkinter Practical Section", font=("Arial", 16))
newLabel.pack(padx=20, pady=20)
textBox = tk.Text(root, height=3, font=("Arial", 16))
textBox.pack()

entery = tk.Entry(root, textvariable="xxxx")
entery.pack()

butonFrame = tk.Frame(root)
butonFrame.columnconfigure(0, weight=1)
butonFrame.columnconfigure(1, weight=1)
butonFrame.columnconfigure(2, weight=1)

b1 = tk.Button(butonFrame, text="Click", font=("Arial", 16))
b1.grid(row=0, column=0, sticky=tk.W+tk.E)

b2 = tk.Button(butonFrame, text="Click2", font=("Arial", 16))
b2.grid(row=0, column=1, sticky=tk.W+tk.E)

b3 = tk.Button(butonFrame, text="Click3", font=("Arial", 16))
b3.grid(row=0, column=2, sticky=tk.W+tk.E)

butonFrame.pack(fill="x")

root.mainloop()


