import sys


special_chars = ['&', '#', '$', '!', '?', '"', '(', ')', '.']

alpha_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 
        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

min_length = 9
max_length = 12
needed_special_chars = 3
needed_alpha_chars = 5
needed_number_count = 3

print("Create your password.")
print("Rules: ")
print(f" 1) Password must be between {min_length} and {max_length} characters")
print(f" 2) Password must contain {needed_alpha_chars} letters [a-zA-Z]")
print(f" 3) Password must contain at least 3 special characters {special_chars}")
password = input("Enter Password: ")
        
special_chars_count = 0
alpha_chars_count = 0
numbers_count = 0

for letter in password:
    if letter in special_chars:
        special_chars_count += 1
    if letter in alpha_chars:
        alpha_chars_count += 1
    if letter.isnumeric():
        numbers_count += 1

if not (max_length >= len(password) >= min_length):
    print(f"Validation Failed: Password length should be between {min_length} and {max_length}")
    exit(0)

if not special_chars_count >= needed_special_chars:
    print(f"Validation Failed: You need to have a minimum of {needed_special_chars} special characters")
    exit(0)

if not alpha_chars_count >= needed_alpha_chars:
    print(f"Validation Failed: You need to have a minimum of {needed_alpha_chars} alpha characters")
    exit(0)

if not numbers_count >= needed_number_count:
    print(f"Validation Failed: You need to have a minimum of {needed_number_count} numbers")
    exit(0)

print("Validation Succeeded!")
