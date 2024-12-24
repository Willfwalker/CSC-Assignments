import re

email = input("Enter your email: ")
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

if re.match(email_pattern, email):
    print("Valid email address.")
else:
    print("Invalid email address.")

text = input("Enter your text: ")
phone_pattern = r'\(\d{3}\)-\d{3}-\d{4}'

masked_text = re.sub(phone_pattern, 'XXX-XXX-XXXX', text)
print("Masked text:", masked_text)

