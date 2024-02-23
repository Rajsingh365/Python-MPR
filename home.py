from tkinter import *
from tkinter import messagebox

import BudgetTracker

def store_data():
    global age, monthly_income, retirement_age, retirement_goal
    age = int(age_entry.get())
    monthly_income = int(income_entry.get())
    retirement_age = int(retirement_age_entry.get())
    retirement_goal = int(retirement_goal_entry.get())

    messagebox.showinfo("Data Stored", f"Age: {age}\nMonthly Income: {monthly_income}\nRetirement Age: {retirement_age}\nRetirement Goal: {retirement_goal}")
    root.destroy()  # Close the first GUI
    BudgetTracker.BudgetTrackercls(monthly_income, retirement_goal, age, retirement_age)

root = Tk()
root.configure(bg='#103359')  # Set background color

# Set default size
root.geometry('800x600')

# Center the window
window_width = root.winfo_reqwidth()
window_height = root.winfo_reqheight()
position_right = int(root.winfo_screenwidth()/2 - window_width/2)
position_down = int(root.winfo_screenheight()/2 - window_height/2)
root.geometry("+{}+{}".format(position_right, position_down))

Label(root, text="Age", bg='#103359', fg='white', font=("Helvetica", 16)).grid(row=0, sticky=E+W)
Label(root, text="Monthly Income", bg='#103359', fg='white', font=("Helvetica", 16)).grid(row=1, sticky=E+W)
Label(root, text="Retirement Age", bg='#103359', fg='white', font=("Helvetica", 16)).grid(row=2, sticky=E+W)
Label(root, text="Retirement Goal", bg='#103359', fg='white', font=("Helvetica", 16)).grid(row=3, sticky=E+W)

age_entry = Entry(root)
income_entry = Entry(root)
retirement_age_entry = Entry(root)
retirement_goal_entry = Entry(root)

age_entry.grid(row=0, column=1)
income_entry.grid(row=1, column=1)
retirement_age_entry.grid(row=2, column =1)
retirement_goal_entry.grid(row=3, column=1)

Button(root, text='Store Data', command=store_data, bg='#103359', fg='white', font=("Helvetica", 16)).grid(row=4, column=0, sticky=W+E, pady=4)

root.mainloop()
