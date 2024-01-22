numbers = []

print("Enter integers (type 'QUIT' to finish):")
while True:
    entry = input()
    if entry == "QUIT":
        break
    numbers.append(int(entry))

even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print("All numbers:", numbers)
print("Even numbers:", even_numbers)
