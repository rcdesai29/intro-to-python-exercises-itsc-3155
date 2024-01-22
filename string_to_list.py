string = input("Enter a string: ")

char_lists = []
for i in range(0, len(string), 3):
    char_lists.append(list(string[i:i+3]))

print("List of character lists:", char_lists)
