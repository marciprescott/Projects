"""Input: User provides two numbers and selects an operation 
(addition, subtraction, multiplication, division).
   Output: The result of the chosen operation."""


def calculate():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation_type = input(
        "Enter type of operation i.e. addition, subtraction, division: "
    )
    if operation_type == "addition":
        result = num1 + num2
    elif operation_type == "subtraction":
        result = num1 - num2
    elif operation_type == "multiplication":
        result = num1 * num2
    elif operation_type == "division":
        if num2 == 0:
            print("Division by zero not allowed!")
        result = num1 / num2

    elif operation_type == "modulo":
        result = num1 % num2

    print("Result:", result)


calculate()
