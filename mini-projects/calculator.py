def main():
    user_input = "y"

    # keep the calculator running in a loop until user types quit
    while user_input == "y":
        # ask the user for the first number
        x = int(input("Enter first number: "))
        # ask the user for the second number
        y = int(input("Enter second number: "))
        # ask the user what operation they want (+, -, *, /)
        operation = input("Enter operation (+, -, *, /): ")

        # if operation is + → add the two numbers
        if operation == "+":
            result = x + y
        # if operation is - → subtract
        elif operation == "-":
            result = x - y
        # if operation is * → multiply
        elif operation == "*":
            result = x * y
        # if operation is / → divide (but check for zero first!)
        elif operation == "/":
            if y == 0:
                return 0
            result = x / y

        # print the result
        print(f"The result is: {result}")

        # if user types quit → stop the loop
        user_input = input(("Another operation? (y for yes, q for quit): "))

main()