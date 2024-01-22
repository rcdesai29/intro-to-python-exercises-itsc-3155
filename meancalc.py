n = int(input("How many numbers will you enter? "))

numbers = []


for i in range(n):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)

total = 0
for num in numbers:
    total += num

mean = total / n

print("Numbers:", numbers)
print("Mean:", mean)
