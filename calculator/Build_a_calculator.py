def main():
    #This loops makes it so that if the user enters a wrong calculation it redoes the process
    while True:
        # Asks what type of operation the user wants to do
        question = input("Would you like to Multiply (m), Divide (d), Add (a), or Subtract (s)? ").lower()

        # Multiplication calculator
        if question == "m":
            x = float(input("What is your first number? "))
            y = float(input("What is your second number? "))
            print(x * y)
            question2 = input("Would you like to do another calculation? (y/n)")
            if question2 == "n":
                break  # Ask if the user wants to do another calculation if not then ends the program

        # Division calculator
        elif question == "d":
            x = float(input("What is your first number? "))
            y = float(input("What is your second number? "))
            print(x / y)
            question3 = input("Would you like to do another calculation? (y/n)")
            if question3 == "n":
                break  # Ask if the user wants to do another calculation if not then ends the program

        # Addition calculator
        elif question == "a":
            x = float(input("What is your first number? "))
            y = float(input("What is your second number? "))
            print(x + y)
            question4 = input("Would you like to do another calculation? (y/n)")
            if question4 == "n":
                break  # Ask if the user wants to do another calculation if not then ends the program

        # Subtraction calculator
        elif question == "s":
            x = float(input("What is your first number? "))
            y = float(input("What is your second number? "))
            print(x - y)
            question5 = input("Would you like to do another calculation? (y/n)")
            if question5 == "n":
                break  # Ask if the user wants to do another calculation if not then ends the program

        # If the user enters a non-valid operation, it prints this error message
        else:
            print("That is not a valid operation. Please enter one of the options.")
    
if __name__ == "__main__":
    main()