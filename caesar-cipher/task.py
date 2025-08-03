import string

alphabet = list(string.ascii_lowercase)

def encrypt(original_text,shift_amount):
    encrypted_text = ""
    for letter in original_text:
        encrypted_index = alphabet.index(letter) + shift_amount
        encrypted_index %= len(alphabet)
        encrypted_text += alphabet[encrypted_index]
    print(f"{encrypted_text}\n")

def decrypt(encrypted_text,shift_amount):
    encrypt(encrypted_text,-shift_amount)

print("Welcome to Caesar Cipher program.\n\n")
text = input("Enter text to encode with the Caesar Cipher: ")
shift = int(input("Enter the number of characters to shift forward: "))

encrypt(text,shift)

text = input("Enter text to decode with the Caesar Cipher: ")
shift = int(input("Enter the number of characters to shift back: "))

decrypt(text,shift)
