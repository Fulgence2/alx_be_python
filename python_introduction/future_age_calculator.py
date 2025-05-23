try:
	input = int(input("How old are you?"))
except ValueError:
    print("Please enter a valid number.")

age = input + 27

print("In 2050, you will be ",age, "years old.")
