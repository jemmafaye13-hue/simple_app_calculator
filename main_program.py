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
            try:
                if choice not in self.operations:
                    print("Invalid Choice!")
                    continue
                num1 = float(input("Num 1: "))
                num2 = float(input("Num 2: "))
                print(f"Result: {self.operations[choice].calculate(num1, num2)}")

            except (ValueError, ZeroDivisionError) as e:
                print(f"Error occurred: {e}")
            finally:
                if input("\nTry again? (y/n): ").lower() != 'y':
                    print("Exiting... Salamat!")
                    break

if __name__ == "__main__":
    app = CalculatorApp()
    app.run()

