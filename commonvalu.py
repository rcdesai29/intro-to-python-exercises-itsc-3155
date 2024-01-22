list1 = []
list2 = []

print("Enter 5 integers for the first list:")
for i in range(5):
    num = int(input(f"Enter integer {i + 1}: "))
    list1.append(num)

print("Enter 5 integers for the second list:")
for i in range(5):
    num = int(input(f"Enter integer {i + 1}: "))
    list2.append(num)


common = []
for num in list1:
    if num in list2 and num not in common:
        common.append(num)

print("List 1:", list1)
print("List 2:", list2)
print("Common elements:", common)
