from tkinter import *
from tkinter import ttk

'''
USE CASE DIAGRAM
what someone can do?
- Click a Number
        --> in this case I want to:
            - Get Entry Value
            - Put New Value to Right
            - Clear Entry
            - Insert New Value
            - [Start Entry as Clear]

- Click a Math Button
        --> in this case I want to:
            - Value in Entry?
            - Store Math Button
            - Store Current Entry Value
            - Clear Entry Widget
            - Prepare for Next Entry
            - [Make Everything a Float]

- Click on Equal Button
         --> in this case I want to:
            - Was Math Clicked?
            - Get 1st Value Entered
            - Get Current Entry Value
            - Perform the Calculation
            - Clear Entry Widget
            - Show Solution to Entry Widget

- Click on Clear Button (AC)
         --> in this case I want to:
            - Clear Math Clicked
            - Clear Entry
            - Put 0 in Entry
            - Put 0 in Current Value

'''

class Calculator:
    calc_value = 0.0
    div_trigger = False
    mult_trigger = False
    add_trigger = False
    sub_trigger = False

    # press button and AC button
    def button_press(self, value):

        if value == 'AC':
            self.div_trigger = False
            self.mult_trigger = False
            self.add_trigger = False
            self.sub_trigger = False
            self.number_entry.delete(0, "end")
            entry_val = 0
            
        else:
            entry_val = self.number_entry.get()
            entry_val+= value
            self.number_entry.delete(0, "end")
            self.number_entry.insert(0, entry_val)


    # press any math button

    def is_float(self, str_value):
        try:
            float(str_value)
            return True
        except ValueError:
            return False

    def math_button_press(self, value):
        if self.is_float(str(self.number_entry.get())):
            self.div_trigger = False
            self.mult_trigger = False
            self.add_trigger = False
            self.sub_trigger = False
            self.calc_value = float(self.entry_value.get())
            if value == "/":
                self.div_trigger = True

            elif value == "*":
                self.mult_trigger = True

            elif value == "+":
                self.add_trigger = True

            else:
                self.sub_trigger = True

            self.number_entry.delete(0, "end")


    def equal_button_press(self):
        if self.add_trigger or self.sub_trigger or self.mult_trigger or self.div_trigger:
            if self.add_trigger:
                solution = self.calc_value + float(self.entry_value.get())
            elif self.sub_trigger:
                solution = self.calc_value - float(self.entry_value.get())
            elif self.mult_trigger:
                solution = self.calc_value * float(self.entry_value.get())
            else:
                solution = self.calc_value / float(self.entry_value.get())

            self.number_entry.delete(0, "end")
            self.number_entry.insert(0, solution)


    def __init__(self, root):
        self.entry_value = StringVar(root, value='')

        root.title("Calculator")
        root.geometry("480x220")
        root.resizable(width=False, height=False)
        style = ttk.Style()
        style.configure("TButton",
                        font="Serif 15",
                        padding=10)
        style.configure("TEntry",
                        font="Courier 18",
                        padding=10)

        self.number_entry = ttk.Entry(root, textvariable= self.entry_value)
        self.number_entry.grid(row=0, columnspan=5, sticky=(W, E))

        self.button7 = ttk.Button(root, text="7", command=lambda: self.button_press('7')).grid(row=1, column=0, sticky=(W, E))
        self.button8 = ttk.Button(root, text="8", command=lambda: self.button_press('8')).grid(row=1, column=2, sticky=(W, E))
        self.button9 = ttk.Button(root, text="9", command=lambda: self.button_press('9')).grid(row=1, column=3, sticky=(W, E))
        self.button_div = ttk.Button(root, text="/", command=lambda: self.math_button_press('/')).grid(row=1, column=4, sticky=(W, E))

        self.button4 = ttk.Button(root, text="4", command=lambda: self.button_press('4')).grid(row=2, column=0, sticky=(W, E))
        self.button5 = ttk.Button(root, text="5", command=lambda: self.button_press('5')).grid(row=2, column=2, sticky=(W, E))
        self.button6 = ttk.Button(root, text="6", command=lambda: self.button_press('6')).grid(row=2, column=3, sticky=(W, E))
        self.button_molt = ttk.Button(root, text="*", command=lambda: self.math_button_press('*')).grid(row=2, column=4, sticky=(W, E))

        self.button1 = ttk.Button(root, text="1", command=lambda: self.button_press('1')).grid(row=3, column=0, sticky=(W, E))
        self.button2 = ttk.Button(root, text="2", command=lambda: self.button_press('2')).grid(row=3, column=2, sticky=(W, E))
        self.button3 = ttk.Button(root, text="3", command=lambda: self.button_press('3')).grid(row=3, column=3, sticky=(W, E))
        self.button_add = ttk.Button(root, text="+", command=lambda: self.math_button_press('+')).grid(row=3, column=4, sticky=(W, E))

        self.button_clear = ttk.Button(root, text="AC", command=lambda: self.button_press('AC')).grid(row=4, column=0, sticky=(W, E))
        self.button0 = ttk.Button(root, text="0", command=lambda: self.button_press('0')).grid(row=4, column=2, sticky=(W, E))
        self.button_equal = ttk.Button(root, text="=", command=lambda: self.equal_button_press()).grid(row=4, column=3, sticky=(W, E))
        self.button_sub = ttk.Button(root, text="-", command=lambda: self.math_button_press('-')).grid(row=4, column=4, sticky=(W, E))





root = Tk()
calc = Calculator(root)

root.mainloop()