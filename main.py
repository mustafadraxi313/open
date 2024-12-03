# main.py
"""
Main script for Git Evaluation Test project.
This script serves as an entry point for a simple application.
"""

# Function Definitions
def greet_user(name):
    """Function to greet the user."""
    print(f"Hello, {name}! Welcome to the Git Evaluation Test.")

def add_numbers(a, b):
    """Function to add two numbers and return the result."""
    return a + b

def display_menu():
    """Function to display the main menu."""
    print("\nMain Menu:")
    print("1. Greet User")
    print("2. Add Numbers")
    print("3. Exit")

# Main Function
def main():
    """Main entry point of the script."""
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter your name: ")
            greet_user(name)
        elif choice == '2':
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                result = add_numbers(num1, num2)
                print(f"The result is: {result}")
            except ValueError:
                print("Invalid input! Please enter numeric values.")
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Execute main function
if __name__ == "__main__":
    main()
