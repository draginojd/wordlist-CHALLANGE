

with open("suffled_words_wordlist.txt", "r") as file:
    contents = file.read()
    shuffled_words = contents.split()
file.close()

print(shuffled_words)