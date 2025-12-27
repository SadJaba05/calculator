# -*- coding: utf8 -*-
import ctypes
import tkinter as tk
from tkinter import messagebox
from math import sqrt
ctypes.windll.shcore.SetProcessDpiAwareness(2)

class Calculator:
    def __init__(self, calc_window):
        self.calc_window = calc_window
        self.calc_window.title('Калькулятор')
        self.calc_window.geometry('700x730')
        self.calc_window.resizable(False, False)
        self.result = '0'
        self.math = ''
        self.f_num = None
        self.frame = tk.Frame(calc_window, bd=2, relief=tk.RAISED)
        self.frame.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        self.display = tk.Label(self.frame, text=self.result, width=24, height=2, font=('Arial', 30), anchor='e', bg='lightgray')
        self.display.pack()
        buttons = [
            '%', 'CE', 'C', '←',
            '1/x', 'x²', '√', '÷',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '±', '0', '.', '=']
        for i, button in enumerate(buttons):
            btn = tk.Button(calc_window, text=button, width=10, height=3, command=lambda b=button: self.on_button_click(b), font=('Arial', 12, 'bold'))
            btn.grid(row=(i // 4) + 1, column=i % 4, sticky='nsew')
        for i in range(4): calc_window.grid_columnconfigure(i, weight=1)
        for i in range(5): calc_window.grid_rowconfigure(i, weight=1)
        self.calc_window.bind('<Key>', self.key_pressed)

    def key_pressed(self, event):
        key = event.keysym
        if key in '0123456789':
            self.on_button_click(key)
        elif key in ['plus', 'minus', 'multiply', 'slash']:
            self.on_button_click('+' if key == 'plus' else
                                 '-' if key == 'minus' else
                                 '*' if key == 'multiply' else '÷')
        elif key == 'Return':
            self.on_button_click('=')
        elif key == 'period':
            self.on_button_click('.')
        elif key == 'c' or key == 'C':
            self.on_button_click('C')
        elif key == 'BackSpace':
            self.on_button_click('←')
        elif key == 'Escape':
            self.on_button_click('CE')
        elif key == 'F6':
            self.on_button_click('√')
        elif key == 'F7':
            self.on_button_click('x²')
        elif key == 'F8':
            self.on_button_click('1/x')
        elif key == '%':
            self.on_button_click('%')
        elif key == 'F5':
            self.on_button_click('±')

    def on_button_click(self, button):
        if button in '0123456789':
            if self.result == '0' and len(self.result) < 20:
                self.result = button
            elif len(self.result) < 20:
                self.result += button
        elif button in ['+', '-', '*', '÷']:
            self.f_num = float(self.result)
            self.math = button
            self.result = '0'
        elif button == '=':
            second_number = float(self.result)
            if self.math == '+':
                self.result = str(self.f_num + second_number)
            elif self.math == '-':
                self.result = str(self.f_num - second_number)
            elif self.math == '*':
                self.result = str(self.f_num * second_number)
            elif self.math == '÷':
                self.result = str(self.f_num / second_number)
        elif button == '.':
            if '.' not in self.result and len(self.result) < 19:
                self.result += '.'
        elif button == 'C':
            self.result = '0'
            self.math = ''
            self.f_num = None
        elif button == 'CE':
            self.result = '0'
        elif button == '√':
            self.result = str(sqrt(float(self.result)))
        elif button == '1/x':
            self.result = str(1 / float(self.result))
        elif button == 'x²':
            self.result = str(float(self.result) ** 2)
        elif button == '±':
            self.result = str(-float(self.result))
        elif button == '←':
            self.result = self.result[:-1] if len(self.result) > 1 else '0'
        elif button == '%':
            self.result = str(float(self.result) / 100.0)
        self.display.config(text=self.result)

if __name__ == '__main__':
    main_window = tk.Tk()
    Calculator(main_window)
    main_window.mainloop()
