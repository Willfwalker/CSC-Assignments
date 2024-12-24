try:
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your Second number: "))
    results = num1 / num2
    print(f"Results: {results}")
except:
    print("Cannnot divide by zero")
class rangeerror(Exception):
    pass

try:
    num = int(input("enter a number between 1-10: "))
    if num < 1 or num > 10:
        raise rangeerror("Number out of range")
    print(f"valid number: {num}")

except rangeerror as e:
    print(e)

