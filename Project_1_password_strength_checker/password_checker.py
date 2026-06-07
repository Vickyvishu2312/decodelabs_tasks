password = input("Enter a password: ")

length = len(password)

upper = False
digit = False
symbol = False

symbols = "!@#$%^&*()-_=+[]{};:',.<>?/"

for ch in password:
    if ch.isupper():
        upper = True
    elif ch.isdigit():
        digit = True
    elif ch in symbols:
        symbol = True

score = 0

if length >= 8:
    score += 1

if upper:
    score += 1

if digit:
    score += 1

if symbol:
    score += 1

print("\nPassword Analysis")

if score <= 1:
    print("Password Strength : Weak")
elif score <= 3:
    print("Password Strength : Medium")
else:
    print("Password Strength : Strong")