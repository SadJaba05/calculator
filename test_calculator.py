import unittest
import tkinter as tk
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.calc = Calculator(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_addition(self):
        self.calc.result = '5'
        self.calc.f_num = 3
        self.calc.math = '+'
        self.calc.on_button_click('=')
        self.assertEqual(self.calc.result, '8.0')

    def test_subtraction(self):
        self.calc.result = '5'
        self.calc.f_num = 10
        self.calc.math = '-'
        self.calc.on_button_click('=')
        self.assertEqual(self.calc.result, '5.0')

    def test_square_root(self):
        self.calc.result = '16'
        self.calc.on_button_click('√')
        self.assertEqual(self.calc.result, '4.0')

if __name__ == '__main__':
    unittest.main()
