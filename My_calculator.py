from tkinter import *
from tkinter import ttk
from math import sqrt, pow


class MyCalculator():

    calc_val = 0.0
    operator = ''
    solution = 0.0

    # All functions
    def btn_press(self, number):
        self.display_math.delete(0, "end")
        self.entry_variable = self.display_number.get()
        self.entry_variable += number
        self.display_number.delete(0, "end")
        self.display_number.insert(0, self.entry_variable)
        #print(self.entry_variable)

    def btn_math(self, oper):
        if self.display_number.get() != '':
            self.calc_val = float(self.display_number.get())
            self.display_number.delete(0, "end")
            self.operator = oper
            #print(self.calc_val)
        else:
            raise self.display_number.insert(0, "Error")

    def btn_math_equal(self):
        if self.operator != '':
            #print(self.calc_val, self.operator, float(self.display_number.get()))
            if self.operator == '+':
                self.solution = self.calc_val + float(self.display_number.get())
            if self.operator == '-':
                self.solution = self.calc_val - float(self.display_number.get())
            if self.operator == '*':
                self.solution = self.calc_val * float(self.display_number.get())
            if self.operator == '/':
                try:
                    self.solution = self.calc_val / float(self.display_number.get())
                except ZeroDivisionError:
                    self.solution = "Cannot divide by 0!!!"
            if self.operator == '^':
                self.solution = pow(self.calc_val, float(self.display_number.get()))
            displays = f'{str(self.calc_val)} {self.operator} {str(float(self.display_number.get()))}'
            self.display_math.insert(0, displays)
            self.display_number.delete(0, "end")
            self.display_number.insert(0, self.solution)
            self.calc_val = self.solution
            self.operator = ''

    def btn_math_sqrt(self, oper):
        if oper == '√':
            self.calc_val = float(self.display_number.get())
            self.solution = sqrt(self.calc_val)
            #print(self.calc_val)
        displays = str(self.calc_val) + oper
        self.display_math.insert(0, displays)
        self.display_number.delete(0, "end")
        self.display_number.insert(0, self.solution)
        self.calc_val = self.solution
        self.operator = ''

    def btn_clear(self):
        self.display_number.delete(0, "end")
        self.display_math.delete(0, "end")
        self.calc_val = 0.0
        self.operator = ''

    def __init__(self, root):
        # Main variable

        self.entry_variable = StringVar(root, value="")

        # Main window
        root.title("My Calculator")
        root.geometry("332x270")
        root.resizable(width=False, height=False)

        # Style of buttons and entry
        style = ttk.Style()
        style.configure("TButton", font=("Arial", 15), padding=7, width=3)
        style.configure("TEntry", padding=5)

        # Row 0
        self.display_number = ttk.Entry(root,
                                        font=("Arial", 15),
                                        textvariable=self.entry_variable,
                                        justify='right',
                                        width=25)
        self.display_number.grid(row=0, columnspan=5, padx=20, pady=5)
        # Row 1
        self.display_math = ttk.Entry(root,
                                        font=("Arial", 10),
                                        justify='right',
                                        width=25)
        self.display_math.grid(row=1, columnspan=5, padx=5)
        # Row 2
        self.button7 = ttk.Button(root, text='7', command=lambda: self.btn_press('7')).grid(row=2, column=0)
        self.button8 = ttk.Button(root, text='8', command=lambda: self.btn_press('8')).grid(row=2, column=1)
        self.button9 = ttk.Button(root, text='9', command=lambda: self.btn_press('9')).grid(row=2, column=2)
        self.button_division = ttk.Button(root, text='/', command=lambda: self.btn_math('/')).grid(row=2, column=3)
        self.button_root = ttk.Button(root, text='√', command=lambda: self.btn_math_sqrt('√')).grid(row=2, column=4)
        # Row 3
        self.button4 = ttk.Button(root, text='4', command=lambda: self.btn_press('4')).grid(row=3, column=0)
        self.button5 = ttk.Button(root, text='5', command=lambda: self.btn_press('5')).grid(row=3, column=1)
        self.button6 = ttk.Button(root, text='6', command=lambda: self.btn_press('6')).grid(row=3, column=2)
        self.button_multi = ttk.Button(root, text='*', command=lambda: self.btn_math('*')).grid(row=3, column=3)
        self.button_power = ttk.Button(root, text='^', command=lambda: self.btn_math('^')).grid(row=3, column=4)
        # Row 4
        self.button1 = ttk.Button(root, text='1', command=lambda: self.btn_press('1')).grid(row=4, column=0)
        self.button2 = ttk.Button(root, text='2', command=lambda: self.btn_press('2')).grid(row=4, column=1)
        self.button3 = ttk.Button(root, text='3', command=lambda: self.btn_press('3')).grid(row=4, column=2)
        self.button_subs = ttk.Button(root, text='-', command=lambda: self.btn_math('-')).grid(row=4, column=3)
        self.button_equal = ttk.Button(root, text='=',
                                       command=lambda: self.btn_math_equal()
                                       ).grid(row=4, column=4)
        # Row 5
        self.button0 = ttk.Button(root, text='0', width=9,
                                  command=lambda: self.btn_press('0')
                                  ).grid(row=5, columnspan=2)
        self.button_point = ttk.Button(root, text=',', command=lambda: self.btn_press('.')).grid(row=5, column=2)
        self.button_plus = ttk.Button(root, text='+', command=lambda: self.btn_math('+')).grid(row=5, column=3)
        self.button_clear = ttk.Button(root, text='AC',
                                       command=lambda: self.btn_clear()
                                       ).grid(row=5, column=4)


# create the application
root = Tk()
calculator = MyCalculator(root)

# start the application
root.mainloop()
