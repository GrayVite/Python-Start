import string
import random

chars = string.punctuation + string.digits + string.ascii_letters + " "
chars = list(chars)

key = chars.copy()

random.shuffle(key)

#ENCRYPTION

plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)  # We find the index in chars where that letter is
    cipher_text += key[index]  # We place a character from key for that corresponding index

print(f"Original Message: {plain_text}")
print(f"Encrypted Message: {cipher_text}")

#DECRYPTION

cipher_text = input("Enter a message to decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter) # We find the index of that letter in key
    plain_text += chars[index] # We find the character at that index and place it 

print(f"Cipher Message: {cipher_text}")
print(f"Decrypted Message: {plain_text}")