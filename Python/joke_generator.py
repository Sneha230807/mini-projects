import random
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "What do you call a fake noodle? An impasta!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "What do you call a bear with no teeth? A gummy bear!",
    "Why don't skeletons fight each other? They don't have the guts!"
]
print("Joke Generator")
while True:
    input("Press Enter to get a random joke ")
    print(random.choice(jokes))
    print()
