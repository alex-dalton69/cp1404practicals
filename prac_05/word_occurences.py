word_to_count = {}
sentence = input("Text: ")
words_in_sentence = sentence.split()
for word in words_in_sentence:
    frequency_of_word = word_to_count.get(word, 0)
    word_to_count[word] = frequency_of_word + 1
words = list(word_to_count.keys())
words.sort()
max_len = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_len, word_to_count[word]))
