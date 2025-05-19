class Calculator:
    def calculate(self, a: float, b: float, operation: str) -> float:
        operation = operation.lower()
        if operation == "addition" or operation == "add":
            return a + b
        elif operation == "subtraction" or operation == "subtract":
            return a - b
        elif operation == "multiplication" or operation == "multiply":
            return a * b
        elif operation == "division" or operation == "divide":
            if b == 0:
                raise ValueError("Cannot divide by zero")
            return a / b
        else:
            raise ValueError("Invalid operation")

# Example usage:
calc = Calculator()
print(calc.calculate(5, 3, "add"))        # Output: 8
print(calc.calculate(5, 3, "subtract"))   # Output: 2
print(calc.calculate(5, 3, "multiply"))   # Output: 15
print(calc.calculate(6, 3, "divide"))     # Output: 2