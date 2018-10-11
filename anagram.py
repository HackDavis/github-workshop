import random

with open('words.txt', "r") as words:
    all_words = words.readlines()

words = random.sample(all_words, 150)
anagrams = list()

for word in words:
    if len(word) < 4:
        continue
    word = word.rstrip('\n')
    print(word)
    word_as_letters = list(word)
    random.shuffle(word_as_letters)
    new_word = ("").join(word_as_letters) + '\n'
    print(new_word)
    anagrams.append(new_word)

with open("anagrams.txt", "w") as anagram_file:
    anagram_file.writelines(anagrams)