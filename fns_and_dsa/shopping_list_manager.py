def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            add = input("Enter the item to add: ")
            shopping_list.append(add)
            print(f"Your current shopping list has the following items: {', '.join(shopping_list)}")
        elif choice == '2':
            # Prompt for and remove an item
            removed = input("Enter the name of the item to be removed: ").lower()
            for item in shopping_list:
                if item.lower() == removed:
                    shopping_list.remove(item)
                    break
            print(f"You have removed the follwing item from your list: {removed}")
            print(f"Your current shopping list has the following items: {', '.join(shopping_list)}")
        elif choice == '3':
            # Display the shopping list
            print(f"Your current shopping list contains {', '.join(shopping_list)}")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()