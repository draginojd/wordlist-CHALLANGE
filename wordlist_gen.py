import re

word_string = "methionyl­threonyl­threonyl­glutaminyl­alanyl­prolyl­threonyl­phenylalany"

# replace non-breaking hyphens with regular hyphens
word_string = word_string.replace("­", "-")

# split the string into a list of words
words = word_string.split("-")

# print each word on a new line
with open("english_wordlist.txt", "w") as file:
    for word in words:
        file.write(word + "\n")
       # print(word)
 