rows = 5
i = 1

while i <= rows:
    # Print spaces
    spaces = rows - i
    j = 1
    while j <= spaces:
        print(" ", end="")
        j += 1

    # Print asterisks
    k = 1
    while k <= (2 * i - 1):
        print("*", end="")
        k += 1

    print()  # Move to next line
    i += 1