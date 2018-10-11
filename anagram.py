from collections import defaultdict
from random import sample, shuffle


def shuffle_word(word):
    stripped_word = word.rstrip('\n')
    letters = list(stripped_word)
    shuffle(letters)
    randomized_word = ('').join(letters)
    if (randomized_word == stripped_word):
        return None
    return randomized_word + '\n'


with open('words.txt', 'r') as words:
    words = words.readlines()

words = sample(words, 300)

filtered_words = filter(lambda word: len(word.rstrip('\n')) >= 4, words)
anagrams = map(shuffle_word, filtered_words)
filtered_anagrams = filter(lambda anagram: anagram != None, anagrams)

anagram_buckets = defaultdict(list)
for anagram in filtered_anagrams:
    anagram_buckets[len(anagram.rstrip('\n'))].append(anagram)

for anagram_length, anagrams in anagram_buckets.items():
    with open(
            '{anagram_length}_letter_anagrams.txt'.format(
                anagram_length=anagram_length),
            'w') as anagram_file:
        anagram_file.writelines(anagrams)
