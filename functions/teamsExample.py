import tkinter as tk
from tkinter import ttk

def teamsExample(pageFrame):
    frame = tk.Frame(pageFrame)
    frame.pack(fill=tk.BOTH, expand=True)
    pageTitle = tk.Label(frame, text="Teams Example", font=("Helvetica", 30))
    pageTitle.place(x=5, y=5)