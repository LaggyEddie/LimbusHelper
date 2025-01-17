import tkinter as tk
from tkinter import ttk

def sinner(pageFrame):
    frame = tk.Frame(pageFrame)
    frame.pack(fill=tk.BOTH, expand=True)
    pageTitle = tk.Label(frame, text="Sinner", font=("Helvetica", 30))
    pageTitle.place(x=5, y=5)