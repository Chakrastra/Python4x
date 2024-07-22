#Word Frequency Counter

import string
# import os

# cur_dir='C:\Users\hp\OneDrive\Desktop\VScode\Python4x\Day5'
# os.chdir(cur_dir)
def count_word_freq(filename):
    with open(filename, 'r') as file:
        text = file.read().lower()
    text = text.translate(str.maketrans("","", string.punctuation))
    words = text.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

path='Day5\sample.txt'
result = count_word_freq(path)

def print_freq(frequencies):
    print("{")
    for word, count in frequencies.items():
        print(f"    '{word}': {count},")
    print("}")

print_freq(result)






