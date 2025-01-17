import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta

def enkephalinRecharge(pageFrame):
    frame = tk.Frame(pageFrame)
    frame.pack(fill=tk.BOTH, expand=True)
    pageTitle = tk.Label(frame, text="Enkephalin Recharge", font=("Helvetica", 30))
    pageTitle.place(x=5, y=5)
    
    def timeToMax():
        try:
            maxEnk = int(maxEnkephalinEntry.get())
            currentEnk = int(currentEnkephalinEntry.get())
            enkNeeded = maxEnk - currentEnk
            timeNeeded = enkNeeded * 6
            
            now = datetime.now()
            maxedTime = now + timedelta(minutes=timeNeeded)
            maxedTimeStr = maxedTime.strftime('%I:%M %p')
            
            maxedTimeLb.config(text="Your Enkephalin will be maxed at " + maxedTimeStr)
        except ValueError:
            maxedTimeLb.config(text="Please enter valid numbers for Enkephalin values.")
        
    def currentTime():
        now = datetime.now().strftime('%I:%M:%S %p')
        currentTimeLb.config(text="Current time: " + now)
        frame.after(1000, currentTime)
    
    # Current time
    currentTimeLb = tk.Label(frame, text="", font=("Arial", 25))
    currentTimeLb.pack(padx=20, pady=20)
    currentTimeLb.place(y=75)
    currentTime()
    
    # Max Enkephalin
    maxEnkephalinLb = tk.Label(frame, text="Max Enkephalin: ", font=("Arial", 18))
    maxEnkephalinLb.place(x=5, y=120)
    maxEnkephalinEntry = ttk.Entry(frame)
    maxEnkephalinEntry.place(x=250, y=120)

    # Current Enkephalin label and entry
    currentEnkephalinLb = tk.Label(frame, text="Current Enkephalin: ", font=("Arial", 18))
    currentEnkephalinLb.place(x=5, y=170)
    currentEnkephalinEntry = ttk.Entry(frame)
    currentEnkephalinEntry.place(x=250, y=170)
    
    # Calculate button
    calculateButton = ttk.Button(frame, text="Calculate Max Time", command=timeToMax)
    calculateButton.bind('<Return>',lambda event:timeToMax())
    calculateButton.place(x=5, y=220, width=170, height=40)
    
    # Maxed Enkephalin result
    maxedTimeLb = tk.Label(frame, text="", font=("Arial", 15))
    maxedTimeLb.place(x=5, y=300)