def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calc(a, o, b):
    """Perform basic math (addition, subtraction, multiplication, division) on a & b input parameters."""
    return operations[o](a, b)

print("Welcome to the Calc program!")

more_calculations = "y"

operand_1 = float(input("What's the first number? "))

while more_calculations == "y":
    operation = input("+\n-\n*\n/\nPick an operation: ")
    operand_2 = float(input("What's the second number? "))
    operand_1 = calc(operand_1, operation, operand_2)

    more_calculations = input(f"Type 'y' to continue calculating with {operand_1}, or type 'n' to start a new calculation: ").lower()
