import random

secret_number = random.randint(1, 10)

guess = int(input("Guess a number: "))

match guess:
    case _ if guess == secret_number:
        print("Secret number is ", secret_number)
        print("🎉 Congratulations, you guessed it!")
    
    case _ if guess > secret_number:
        print("Secret number is ", secret_number)
        print("Oops, your guess is a bit high. Try again!")

    case _ if guess < secret_number:
        print("Secret number is ", secret_number)
        print("Nope, your guess is a bit low. Give it another shot!")

    case _:
        print("You guessed wrong")
        print("Secret number is ", secret_number)


play_again = input("Do you want to play again? (yes/no): ").strip().lower()
if play_again != "yes":
        print("Thanks for playing! 👋")