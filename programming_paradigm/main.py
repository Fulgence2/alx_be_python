import sys
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
    
# including error handling for division by zero.
# It can be used from the command line to perform division operations.
# This code is intended to be run from the command line, where it takes two arguments: numerator and denominator.
# It performs division and handles division by zero errors gracefully.
# It can also be used as a module in other Python scripts.
# This code is intended to be run from the command line, where it takes two arguments: numerator and denominator.
# It performs division and handles division by zero errors gracefully.
# It can also be used as a module in other Python scripts.
# This code is intended to be run from the command line, where it takes two arguments: numerator and denominator.
# It performs division and handles division by zero errors gracefully.
# It can also be used as a module in other Python scripts. 