#!/bin/python3
"""
Styled Tkinter GUI
"""
import re
import tkinter as tk
from tkinter import messagebox

class MyGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Practical Section - Tkinter")
        self.root.geometry("600x700")

        self.root.configure(bg="#f0f0f0")

        headerFrame = tk.Frame(self.root, bg="#3498db", padx=20, pady=20)
        headerFrame.pack(fill=tk.X)

        self.newLabel = tk.Label(headerFrame, text="Welcome to Tkinter Practical Section", 
                                 font=("Segoe UI Black", 18), fg="#ffffff", bg="#3498db")
        self.newLabel.pack()

        contentFrame = tk.Frame(self.root, bg="#f5f5f5", padx=40, pady=20)
        contentFrame.pack(fill=tk.BOTH, expand=True)

        self.textBoxFrame = tk.Frame(contentFrame, bg="#ffffff", bd=2, relief="ridge")
        self.textBoxFrame.pack(pady=15, fill=tk.X)

        self.textLabel = tk.Label(self.textBoxFrame, text="Enter your text here --> ", 
                                   font=("Segoe UI", 14), bg="#ffffff")
        self.textLabel.pack(side=tk.LEFT)

        self.textBox = tk.Text(self.textBoxFrame, height=5, font=("Segoe UI", 16))
        self.textBox.pack(fill=tk.X, expand=True)

        optionsFrame = tk.Frame(contentFrame, bg="#ffffff")
        optionsFrame.pack(pady=15)

        self.emailVar = tk.BooleanVar(value=False)
        self.emailCheckbox = tk.Checkbutton(optionsFrame, text="Email", variable=self.emailVar, 
                                             font=("Segoe UI", 12), fg="#3498db", bg="#ffffff", 
                                             activebackground="#e74c3c", activeforeground="#ffffff")
        self.emailCheckbox.pack(anchor=tk.W, pady=5)

        self.phoneVar = tk.BooleanVar(value=False)
        self.phoneCheckbox = tk.Checkbutton(optionsFrame, text="Phone", variable=self.phoneVar, 
                                             font=("Segoe UI", 12), fg="#3498db", bg="#ffffff", 
                                             activebackground="#e74c3c", activeforeground="#ffffff")
        self.phoneCheckbox.pack(anchor=tk.W, pady=5)

        self.hashtagVar = tk.BooleanVar(value=False)
        self.hashtagCheckbox = tk.Checkbutton(optionsFrame, text="Hashtag", variable=self.hashtagVar, 
                                                font=("Segoe UI", 12), fg="#3498db", bg="#ffffff", 
                                                activebackground="#e74c3c", activeforeground="#ffffff")
        self.hashtagCheckbox.pack(anchor=tk.W, pady=5)

        self.buttonFrame = tk.Frame(contentFrame, bg="#f5f5f5")
        self.buttonFrame.pack(pady=15)

        self.submitButton = tk.Button(self.buttonFrame, text="Submit", font=("Segoe UI Black", 16),
                                      fg="#ffffff", bg="#3498db", relief="flat", bd=0,
                                      command=self.show_results)
        self.submitButton.pack()

        self.resultAreaFrame = tk.Frame(contentFrame, bg="#ffffff", bd=2, relief="ridge")
        self.resultAreaFrame.pack(pady=15, fill=tk.BOTH, expand=True)

        self.resultLabel = tk.Label(self.resultAreaFrame, text="Results -->", 
                                    font=("Segoe UI Black", 18))
        self.resultLabel.pack(side=tk.LEFT)

        self.resultArea = tk.Text(self.resultAreaFrame, height=5, font=("Segoe UI", 14))
        self.resultArea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.root.mainloop()

    def show_results(self):
        """
        """
        text = self.textBox.get("1.0", tk.END).strip()
        
        emails = []
        phones = []
        hashtags = []

        if self.emailVar.get():
            pattr = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            emails = re.findall(pattr, text)

        if self.phoneVar.get():
            pattr = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b|\(\d{3}\)\s*\d{3}[-.]?\d{4}\b'
            phones = re.findall(pattr, text)

        if self.hashtagVar.get():
            pattr = r'#\w+'
            hashtags = re.findall(pattr, text)

        result = ""
        if emails:
            result += f"Emails: {', '.join(emails)}\n"
        
        if phones:
            result += f"Phone Numbers: {', '.join(phones)}\n"
        
        if hashtags:
            result += f"Hashtags: {', '.join(hashtags)}"

        if not self.emailVar.get() and not self.phoneVar.get() and not self.hashtagVar.get():
            messagebox.showerror("Error", "Please select at least one option.")
            return
        
        if not self.textBox.get("1.0", tk.END).strip():
            messagebox.showerror("Error", "Please enter some text.")
            return

        if not result:
            result = "No results found."
        self.resultArea.delete("1.0", tk.END)
        self.resultArea.insert(tk.END, result)

if __name__ == "__main__":
    mygui = MyGUI()
