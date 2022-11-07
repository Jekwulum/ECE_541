"""
    ASSIGNMENT NO. 3
    This program runs a simple calculator
"""


def main():
    while True:
        print("----------------------------------------\nWelcome to the simple calculator program")
        operator = get_valid_operator()
        value1 = float(input("Enter the first number: "))
        value2 = float(input("Enter the second number: "))

        result = 0
        if operator == "+":
            result = value1 + value2
        elif operator == "-":
            result = value1 - value2
        elif operator == "*":
            result = value1 * value2
        elif operator == "/":
            result = value1 / value2
        print(f"{value1} {operator} {value2} = {result}")

        is_quitting = input("Do you wish to continue? Y/N").upper()
        if is_quitting == 'N':
            break


def get_valid_operator():
    """gets a valid operator from the user"""
    operator = input("Enter operator (+ - * /): ")
    while operator not in ['+', '-', '/', '*']:
        print("Invalid operator")
        operator = input("Enter operator (+ - * /): ")
    return operator


main()
