def divide(a, b):
    # check muna kung zero yung denominator, bawal mag-divide by zero
    if b == 0:
        print("error: bawal mag-divide by zero.")
        return None
    return a / b  # compute division

def exponentiate(a, b):
    return a ** b  # compute exponentiation

def remainder(a, b):
    # check kung zero yung denominator
    if b == 0:
        print("error: bawal kumuha ng remainder kung zero yung divisor.")
        return None
    return a % b  # compute remainder

def summation(a, b):
    # check kung mas mataas dapat yung second number kesa sa first
    if a > b:
        print("error: yung second number dapat mas malaki sa first.")
        return None
    return sum(range(a, b + 1))  # kunin yung total ng numbers sa range

def menu():
    while True:
        # display ng menu options
        print("\nchoose an operation:")
        print("[D] - divide")
        print("[E] - exponentiation")
        print("[R] - remainder")
        print("[F] - summation")
        print("[Q] - quit")

        choice = input("enter your choice: ").upper()  # gawing uppercase para walang case sensitivity issue

        if choice == 'Q':
            print("exiting program. goodbye!")
            break  # exit na sa loop
        elif choice in ['D', 'E', 'R', 'F']:
            try:
                # kuha ng dalawang numbers from user
                num1 = int(input("enter first number: "))
                num2 = int(input("enter second number: "))

                # check kung anong operation yung pipiliin, then call function
                if choice == 'D':
                    result = divide(num1, num2)
                elif choice == 'E':
                    result = exponentiate(num1, num2)
                elif choice == 'R':
                    result = remainder(num1, num2)
                elif choice == 'F':
                    result = summation(num1, num2)

                # print lang yung result kung hindi siya None
                if result is not None:
                    print("result:", result)

            except ValueError:
                print("invalid input. numbers lang dapat.")  # check kung hindi number yung input
        else:
            print("invalid choice. pili ng tama.")  # kung maling letter yung pinili

# run the program
menu()
