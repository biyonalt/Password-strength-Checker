import re

password = input("Enter your password: ")

strength = 0

# Length check
if len(password) >= 8:
    strength += 1

# Contains number
if re.search(r"\d", password):
    strength += 1

# Contains uppercase
if re.search(r"[A-Z]", password):
    strength += 1

# Contains special character
if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    strength += 1

# Result
if strength == 4:
    print("Strong Password 💪")
elif strength == 3:
    print("Medium Password ⚠️")
else:
    print("Weak Password ❌")
