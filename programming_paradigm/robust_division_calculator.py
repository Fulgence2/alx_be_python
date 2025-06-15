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
        return (f"The result of the division is {float(numerator) / float(denominator)}")
    except ZeroDivisionError:
        return("Error: Cannot divide by zero.")
    except TypeError:
        return("Error: Both numerator and denominator must be numbers.")
    except ValueError:
        return("Error: Please enter numeric values only.")
    except Exception as e:
        return(f"An unexpected error occurred: {e}")
# This function can be used in a command-line interface or imported into other Python scripts.