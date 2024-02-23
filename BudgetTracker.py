from tkinter import *
from tkinter import filedialog
import investment

class BudgetTrackercls:
    def __init__(self, monthly_income, retirement_goal, age, retirement_age):
        self.monthly_income = monthly_income
        self.retirement_goal = retirement_goal
        self.age = age
        self.retirement_age = retirement_age
        self.expenses = 0
        self.monthly_savings = int(monthly_income) - self.expenses
        self.annual_savings = self.monthly_savings * 12

        self.root = Tk()
        self.root.configure(bg='#103359')  # Set background color

        # Set default size
        self.root.geometry('800x600')

        # Center the window
        window_width = self.root.winfo_reqwidth()
        window_height = self.root.winfo_reqheight()
        position_right = int(self.root.winfo_screenwidth()/2 - window_width/2)
        position_down = int(self.root.winfo_screenheight()/2 - window_height/2)
        self.root.geometry("+{}+{}".format(position_right, position_down))

        button = Button(self.root, text="Open File", command=self.calculate_expenses, bg='#103359', fg='white', font=("Helvetica", 16))
        button.pack()

        # Define StringVar variables for savings labels
        self.savings = StringVar()
        self.savings.set("Monthly Savings: " + str(self.monthly_savings))
        self.savings_label = Label(self.root, textvariable=self.savings, bg='#103359', fg='white', font=("Helvetica", 16))

        self.annual_savings_label = Label(self.root, text="Annual Savings: " + str(self.annual_savings), bg='#103359', fg='white', font=("Helvetica", 16))

        investment_button = Button(self.root, text="Go to Investment", command=self.redirect_to_investment, bg='#103359', fg='white', font=("Helvetica", 16))
        investment_button.pack()

        self.root.mainloop()

    def calculate_expenses(self):
        filename = filedialog.askopenfilename()
        if filename == '':
            return  # No file is selected, do nothing
        self.expenses = 0
        try:
            with open(filename, 'r') as file:
                for line in file:
                    try:
                        key, value = line.split(':')
                        self.expenses += int(value)
                    except ValueError:
                        pass
            # Update savings labels after calculating expenses
            self.update_savings_labels()
        except FileNotFoundError:
            print("File Not Found")

    def update_savings_labels(self):
        self.monthly_savings = int(self.monthly_income) - self.expenses
        self.annual_savings = self.monthly_savings * 12

        # Update text of savings labels
        self.savings.set("Monthly Savings: " + str(self.monthly_savings))
        self.annual_savings_label.config(text="Annual Savings: " + str(self.annual_savings))

        # Show the labels
        self.savings_label.pack()
        self.annual_savings_label.pack()

    def redirect_to_investment(self):
        # Call part 2, investment.py
        self.root.destroy()
        app = investment.InvestmentApp(self.age, self.retirement_age, self.monthly_savings, self.retirement_goal)
        app.mainloop()

