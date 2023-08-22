import tkinter as tk
from datetime import datetime

def update_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    time_label.config(text=current_time)
    root.after(1000, update_time)

root = tk.Tk()
root.title("Digital Clock")

time_label = tk.Label(root, font=("Helvetica", 80))
time_label.pack(padx=50, pady=20)

update_time()
root.mainloop()
