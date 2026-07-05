class InvalidOperatorError (Exception):
    """Raised when the operator isn't one of +, -, *, /"""

def __init__(self,operator):
        self.operator=operator
        super().__init__(f" '{operator}' is not a valid operator.")

def calculate(num1,num2,operator):
    if operator== '+':
         return num1 + num2
    elif operator== '-':
         return num1 - num2
    elif operator== '*':
         return num1 * num2
    elif operator== '/':
         return num1 / num2
    else:
        raise InvalidOperatorError(operator)
    
while True:
    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter the operator (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))
        result = calculate(num1, num2, operator)
        print(f"The result is: {result}")
        break
    except InvalidOperatorError as e:
        print(e)
    except ValueError:
        print("Please enter valid numbers.")
    except ZeroDivisionError:
         print("Error: Division by zero is not allowed.")
    finally:
        print("Calculation attempt completed.")

    if input("Calculate again? (y/n): ").lower() != 'y':
        break