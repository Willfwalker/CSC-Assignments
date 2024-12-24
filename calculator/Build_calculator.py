#The functions that do the calculation
def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def power(x, y):
    return x ** y

#Function to find what operation the user wants to use
def get_operation():
    while True:
        operation = input("Would you like to Multiply (m), Divide (d), Add (a), Power (p), or Subtract (s)? ").lower()
        if operation in ['m', 'd', 'a', 's', 'p']:
            return operation
        else:
            print("That is not a valid operation. Please enter one of the options.")

#Function that recieves the the numbers from the users thendoes the calculations
def main():
    while True:
        chosen_operation = get_operation()
        x = float(input("What is your first number? "))
        y = float(input("What is your second number? "))

        if chosen_operation == "m":
            result = multiply(x, y)
        elif chosen_operation == "d":
            result = divide(x, y)
        elif chosen_operation == "a":
            result = add(x, y)
        elif chosen_operation == "s":
            result = subtract(x, y)
        elif chosen_operation == "p":
            result = power(x, y)
        
        print("Your answer is: " + f"{result}")
#Asks the user if they want to do another equation      
        another_calculation = input("Would you like to do another calculation? (y/n) ").lower()
        if another_calculation != 'y':
            break

if __name__ == "__main__":
    main()
