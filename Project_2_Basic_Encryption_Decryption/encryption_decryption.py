message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

encrypted_text = ""

# Encryption
for ch in message:
    if ch.isalpha():

        if ch.isupper():
            new_char = chr(((ord(ch) - 65 + shift) % 26) + 65)
        else:
            new_char = chr(((ord(ch) - 97 + shift) % 26) + 97)

        encrypted_text += new_char

    else:
        encrypted_text += ch

print("\nEncrypted Text:", encrypted_text)

# Decryption
decrypted_text = ""

for ch in encrypted_text:
    if ch.isalpha():

        if ch.isupper():
            new_char = chr(((ord(ch) - 65 - shift) % 26) + 65)
        else:
            new_char = chr(((ord(ch) - 97 - shift) % 26) + 97)

        decrypted_text += new_char

    else:
        decrypted_text += ch

print("Decrypted Text:", decrypted_text)