numbers = []
print("Enter 10 integers:")
for i in range(10):
    num = int(input(f"Enter integer {i + 1}: "))
    numbers.append(num)

unique = []
for num in numbers:
    if numbers.count(num) == 1:
        unique.append(num)

print("Original list:", numbers)
print("Unique elements:", unique)
