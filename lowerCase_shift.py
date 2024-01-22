user_input = input("Enter a string: ")

lowercase_chars = ""
uppercase_chars = ""

for char in user_input:
    if char.islower():
        lowercase_chars += char
    elif char.isupper():
        uppercase_chars += char

result_string = lowercase_chars + uppercase_chars

print("Modified string:", result_string)
