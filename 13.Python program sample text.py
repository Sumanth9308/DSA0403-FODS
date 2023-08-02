import string
from collections import Counter

def calculate_word_frequency(text):
   
    translator = str.maketrans('', '', string.punctuation)
    tokens = text.translate(translator).lower().split()

    word_frequency = Counter(tokens)

    sorted_word_frequency = dict(sorted(word_frequency.items(), key=lambda item: item[1], reverse=True))

    return sorted_word_frequency

def display_word_frequency(word_frequency):
    
    for word, count in word_frequency.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    text = input("Enter the text document: ")
    word_frequency = calculate_word_frequency(text)
    display_word_frequency(word_frequency)
