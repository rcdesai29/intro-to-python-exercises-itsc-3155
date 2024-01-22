words = []

print("Enter 5 words:")
for i in range(5):
    word = input(f"Enter word {i + 1}: ")
    words.append(word)

sentence = ""
for word in words:
    sentence += word + " "

print("Words:", words)
print("Sentence:", sentence.strip())
