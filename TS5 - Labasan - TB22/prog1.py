def divide(a, b):
    # check if the denominator is zero
    if b == 0:
        print("error: cannot divide by zero.")
        return None
    return a / b  # perform division

def exponentiate(a, b):
    return a ** b  # perform exponentiation

def remainder(a, b):
    # check if the denominator is zero
    if b == 0:
        print("error: cannot find remainder with zero.")
        return None
    return a % b  # find remainder

def summation(a, b):
    # check if the second number is greater than the first
    if a > b:
        print("error: the second number must be greater than the first.")
        return None
    return sum(range(a, b + 1))  # compute summation from a to b

def menu():
    while True:
        # display menu options
        print("\nchoose an operation:")
        print("[D] - divide")
        print("[E] - exponentiation")
        print("[R] - remainder")
        print("[F] - summation")
        print("[Q] - quit")

        choice = input("enter your choice: ").upper()  # convert input to uppercase

        if choice == 'Q':
            print("exiting program. goodbye!")
            break  # exit the loop
        elif choice in ['D', 'E', 'R', 'F']:
            try:
                # get user input for numbers
                num1 = int(input("enter first number: "))
                num2 = int(input("enter second number: "))

                # call the appropriate function based on choice
                if choice == 'D':
                    result = divide(num1, num2)
                elif choice == 'E':
                    result = exponentiate(num1, num2)
                elif choice == 'R':
                    result = remainder(num1, num2)
                elif choice == 'F':
                    result = summation(num1, num2)

                # print result if it's not None
                if result is not None:
                    print("result:", result)

            except ValueError:
                print("invalid input. please enter numbers only.")  # handle non-numeric input
        else:
            print("invalid choice. please enter a valid option.")  # handle incorrect choices

# run the program
menu()
