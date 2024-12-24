with open("user_data.txt", "w") as file:
    name = input("Whats your name? ")
    age = input("Whats your Age? ")
    file.write(f"Name: {name} Age: {age}")

with open("user_data.txt", "r") as file:
    content = file.read()
    print("File content:", content)
