import sys

class Operation:
    def calculate(self, num1, num2):
        pass

class Addition(Operation):
    def calculate(self, num1, num2):
        return num1 + num2

class Subtraction(Operation):
    def calculate(self, num1, num2):
        return num1 - num2

class Multiplication(Operation):
    def calculate(self, num1, num2):
        return num1 * num2

class Division(Operation):
    def calculate(self, num1, num2):
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        return num1 / num2

class CalculatorApp:
    def __init__(self):
        self.operations = {
            "1": Addition(),
            "2": Subtraction(),
            "3": Multiplication(),
            "4": Division()
        }

    def run(self):
        print("--- MAANGAS CALCULATOR PRO ---")
        while True:
            print("\n[1] Add [2] Sub [3] Mult [4] Div")
            choice = input("Select Operation (1-4): ")