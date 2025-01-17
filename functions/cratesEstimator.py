import tkinter as tk
from tkinter import ttk

def cratesEstimator(pageFrame):
    frame = tk.Frame(pageFrame)
    frame.pack(fill=tk.BOTH, expand=True)
    pageTitle = tk.Label(frame, text="Crates Estimator", font=("Helvetica", 30))
    pageTitle.place(x=5, y=5)