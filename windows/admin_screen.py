import tkinter as tk
import sys
import os
import threading

def run_sub(): os.system('pythonw windows\\subjects.py')
def run_task(): os.system('pythonw windows\\task_manager_frontend.py')

ad = tk.Tk()
ad.geometry('500x430')

ad.title('Administrator')

tk.Label(
    ad,
    text='ATTENTION BOOST',
    font=('Consolas', 20, 'bold'),
    pady=10
).pack()

modify_frame = tk.LabelFrame(text='Add / Update Tasks', font=('Consolas'), padx=20)
modify_frame.place(x=100, y=100)

tk.Button(
    modify_frame,
    text='Tasks',
    font=('Consolas'),
    command=run_sub
).pack(pady=20)

tk.Button(
    ad,
    text='Quit',
    font=('Consolas'),
    command=ad.destroy
).place(x=220, y=360)

ad.mainloop()