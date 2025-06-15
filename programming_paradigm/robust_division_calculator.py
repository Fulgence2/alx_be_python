def safe_divide(numerator, denominator):
    """
    Safely divides two numbers, handling division by zero and type errors.
    
    Args:
        numerator (float): The number to be divided.
        denominator (float): The number to divide by.
    
    Returns:
        float: The result of the division or None if an error occurs.
    """
    try:
        print(f"The result of the division is {float(numerator) / float(denominator)}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return
    except TypeError:
        print("Error: Both numerator and denominator must be numbers.")
        return
    except ValueError:
        print("Error: Please enter numeric values only.")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return
    return float(numerator) / float(denominator)
# This function can be used in a command-line interface or imported into other Python scripts.