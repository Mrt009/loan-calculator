from tkinter import *

# Import Tk themed widgets
from tkinter import ttk


class Loan_Calculator():

    def __init__(self):
        # creating the root window here
        root = Tk()

        # set the title
        root.title('Loan Calculator')

        # set the geometry
        # root.geometry('250x300')

        # set the background color
        root.config(background='beige')

        # creating the labels
        Label(root, text='Annual Interest Rate', bg='Beige', borderwidth=4).grid(row=1, column=1, sticky=W)

        Label(root, text='Numbers of Years', bg='Beige', borderwidth=4).grid(row=2, column=1, sticky=W)

        Label(root, text='Loan Ammount', bg='Beige', borderwidth=4).grid(row=3, column=1, sticky=W)

        Label(root, text='Monthly Payment', bg='Beige', borderwidth=4).grid(row=4, column=1, sticky=W)

        Label(root, text='Total Payment', bg='Beige', borderwidth=4).grid(row=5, column=1, sticky=W)

        # Create the Entry Widgets
        self.AnnualInterest = StringVar()
        Entry(root, textvariable=self.AnnualInterest, justify=RIGHT).grid(row=1, column=2, sticky=E)

        self.years = StringVar()
        Entry(root, textvariable=self.years, justify=RIGHT).grid(row=2, column=2, sticky=E)

        self.amount = StringVar()
        Entry(root, textvariable=self.amount, justify=RIGHT).grid(row=3, column=2, sticky=E)

        self.monthlyPayment = StringVar()
        Label(root, textvariable=self.monthlyPayment).grid(row=4, column=2, sticky=E)

        self.TotalPayment = StringVar()
        Label(root, textvariable=self.TotalPayment).grid(row=5, column=2, sticky=E)

        # CREATING BUTTONS
        compute = Button(root, text='Compute Loan', command=self.ComputePayment).grid(row=6, column=2, sticky=E)

        root.mainloop()

    # compute the total payment.
    def ComputePayment(self):
        month = self.getMonthlyPayment(
            float(self.amount.get()),
            float(self.AnnualInterest.get()) / 1200,
            int(self.years.get()))

        self.monthlyPayment.set(format(month, '10.2f'))

        total = float(self.monthlyPayment.get()) * 12 * int(self.years.get())

        self.TotalPayment.set(format(total, '10.2f'))

    def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberOfYears):
        # compute the monthly payment.
        month = loanAmount * monthlyInterestRate / (1
                                                    - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
        return month;


Loan_Calculator()

