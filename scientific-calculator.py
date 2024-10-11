import math
import statistics
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def calculator():
    while True:
        # Display colorful menu
        print(Fore.CYAN + Style.BRIGHT + "SIMPLE CALCULATOR")
        print(Fore.CYAN + "---------------------------")
        print(Fore.GREEN + "CHOOSE OPERATION")
        print(Fore.YELLOW + "1. Arithmetic operations")
        print(Fore.YELLOW + "2. Trigonometric operations")
        print(Fore.YELLOW + "3. Statistical operations")
        print(Fore.YELLOW + "4. Other functional operations")
        
        # Get the user's main choice
        main_choice = int(input(Fore.BLUE + "Enter choice (1/2/3/4): "))

        if main_choice == 1:  # Arithmetic operations
            print(Fore.GREEN + "Choose operation")
            print(Fore.YELLOW + "1. Addition")
            print(Fore.YELLOW + "2. Subtraction")
            print(Fore.YELLOW + "3. Multiplication")
            print(Fore.YELLOW + "4. Division")
            print(Fore.YELLOW + "5. Percentage")
            choice1 = int(input(Fore.BLUE + "Enter choice (1/2/3/4/5): "))
            x = float(input(Fore.MAGENTA + "Enter a number: "))
            y = float(input(Fore.MAGENTA + "Enter another number: "))

            if choice1 == 1:  # Add
                total = x + y
                print(Fore.CYAN + f"Result: {total}")

            elif choice1 == 2:  # Subtract
                total2 = x - y
                print(Fore.CYAN + f"Result: {total2}")

            elif choice1 == 3:  # Multiply
                mul = x * y
                print(Fore.CYAN + f"Result: {mul}")

            elif choice1 == 4:  # Divide
                if y != 0:
                    div = x / y
                    print(Fore.CYAN + f"Result: {div}")
                else:
                    print(Fore.RED + "Error: Can't divide by zero")

            elif choice1 == 5:  # Percentage
                if y != 0:
                    per = (x / y) * 100
                    print(Fore.CYAN + f"Result: {per}%")
                else:
                    print(Fore.RED + "Error: Can't divide by zero")

            else:
                print(Fore.RED + "Invalid input!!!")

        elif main_choice == 2:  # Trigonometric operations
            print(Fore.GREEN + "Choose operation")
            print(Fore.YELLOW + "1. Sin")
            print(Fore.YELLOW + "2. Cos")
            print(Fore.YELLOW + "3. Tan")
            print(Fore.YELLOW + "4. Cosec")
            print(Fore.YELLOW + "5. Sec")
            print(Fore.YELLOW + "6. Cot")

            choice2 = int(input(Fore.BLUE + "Enter choice (1/2/3/4/5/6): "))
            z = float(input(Fore.MAGENTA + "Enter the number: "))

            if choice2 == 1:
                print(Fore.CYAN + f"Result: {math.sin(z)}")
            elif choice2 == 2:
                print(Fore.CYAN + f"Result: {math.cos(z)}")
            elif choice2 == 3:
                print(Fore.CYAN + f"Result: {math.tan(z)}")
            elif choice2 == 4:
                if math.sin(z) != 0:
                    print(Fore.CYAN + f"Result: {1 / math.sin(z)}")
                else:
                    print(Fore.RED + "Error: Cannot divide by zero.")
            elif choice2 == 5:
                if math.cos(z) != 0:
                    print(Fore.CYAN + f"Result: {1 / math.cos(z)}")
                else:
                    print(Fore.RED + "Error: Cannot divide by zero.")
            elif choice2 == 6:
                if math.tan(z) != 0:
                    print(Fore.CYAN + f"Result: {1 / math.tan(z)}")
                else:
                    print(Fore.RED + "Error: Cannot divide by zero.")
            else:
                print(Fore.RED + "Invalid input!!!")

        elif main_choice == 3:  # Statistical operations
            print(Fore.GREEN + "Choose operation")
            print(Fore.YELLOW + "1. Mean")
            print(Fore.YELLOW + "2. Median")
            print(Fore.YELLOW + "3. Mode")
            print(Fore.YELLOW + "4. Max")
            print(Fore.YELLOW + "5. Min")

            choice = int(input(Fore.BLUE + "Enter choice: "))

            # Get user input for the tuple
            user_input = input(Fore.MAGENTA + "Enter numbers (comma-separated): ")
            numbers = tuple(map(float, user_input.split(",")))

            if choice == 1:
                print(Fore.CYAN + f"Mean: {statistics.mean(numbers)}")
            elif choice == 2:
                print(Fore.CYAN + f"Median: {statistics.median(numbers)}")
            elif choice == 3:
                print(Fore.CYAN + f"Mode: {statistics.mode(numbers)}")
            elif choice == 4:
                print(Fore.CYAN + f"Max: {max(numbers)}")
            elif choice == 5:
                print(Fore.CYAN + f"Min: {min(numbers)}")
            else:
                print(Fore.RED + "Invalid input!!!")

        elif main_choice == 4:  # Other operations
            print(Fore.GREEN + "Choose operation")
            print(Fore.YELLOW + "1. Logarithm")
            print(Fore.YELLOW + "2. Square Root")
            print(Fore.YELLOW + "3. Exponentiation")

            choice3 = int(input(Fore.BLUE + "Enter choice (1/2/3): "))

            if choice3 == 1:  # Logarithm
                number = float(input(Fore.MAGENTA + "Enter the number: "))
                base = float(input(Fore.MAGENTA + "Enter the base: "))
                print(Fore.CYAN + f"Result: {math.log(number, base)}")
            elif choice3 == 2:  # Square Root
                number = float(input(Fore.MAGENTA + "Enter the number: "))
                print(Fore.CYAN + f"Result: {math.sqrt(number)}")
            elif choice3 == 3:  # Exponentiation
                base = float(input(Fore.MAGENTA + "Enter the base: "))
                exponent = float(input(Fore.MAGENTA + "Enter the exponent: "))
                print(Fore.CYAN + f"Result: {math.pow(base, exponent)}")
            else:
                print(Fore.RED + "Invalid input!!!")
        
        else:
            print(Fore.RED + "Invalid input!!!")
        
        # Ask if the user wants to calculate again
        again = input(Fore.GREEN + "Do you want to calculate again? (yes/no): ").lower()
        if again != "yes":
            print(Fore.CYAN + "Exiting the calculator. Goodbye!")
            break

# Call the calculator function
calculator()
