num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /):")

def calculation(operation, num1, num2):
    match operation:
        case "+":
            result =  num1 + num2
        case "-":
            result = num1 - num2
        case "*":
            result =  num1 * num2
        case "/":
            if num2 != 0:
                result =  num1 / num2
            else:
                print("Error: Division by zero.")
                return
        case _:
            print("I am not able to perform that calculation")
            return

    print(f"The result is {result}.")

calculation(operation, num1, num2)