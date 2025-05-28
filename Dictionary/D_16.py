word_freq = {"apple": 2, "banana": 3}

word = "orange"
word_freq[word] = word_freq.get(word, 0) + 1
print(word_freq)  # Output: {'apple': 2, 'banana': 3, 'orange': 1}
