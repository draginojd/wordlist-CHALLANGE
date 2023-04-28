import time

with open("suffled_words_wordlist.txt", "r") as file:
    contents = file.read()
    shuffled_words = contents.split()
file.close()


start_time = time.time()
print(shuffled_words)
end_time = time.time()
time_passed = end_time - start_time


print("Total time: ", time_passed) 