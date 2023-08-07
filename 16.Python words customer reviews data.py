def calculate_word_frequency(review_text):

    review_text = review_text.lower()

    words = review_text.split()

    words = [word.strip(".,!?()[]{}-\"'") for word in words if word.isalpha()]

    stop_words = set([
        "a", "an", "and", "the", "in", "on", "at", "to", "of", "for", "it", "is", "with", "was", "were", "I", "you", "he", "she", "they", "we"
    ])
    words = [word for word in words if word not in stop_words]

    word_frequency = {}
    for word in words:
        word_frequency[word] = word_frequency.get(word, 0) + 1

    return word_frequency

def main():
    customer_reviews = [
        "This product is amazing. I love it!",
        "The quality is excellent, highly recommended.",
        "Not worth the price. Disappointed with the purchase.",
        "The customer service was terrible, never buying again.",
        "Incredible product. Works as expected.",
        "Great value for money."
    ]
    
    total_word_frequency = {}
    for review in customer_reviews:
        review_frequency = calculate_word_frequency(review)
        for word, frequency in review_frequency.items():
            total_word_frequency[word] = total_word_frequency.get(word, 0) + frequency

    print("Frequency Distribution of Words:")
    for word, frequency in total_word_frequency.items():
        print(f"{word}: {frequency}")

if __name__ == "__main__":
    main()
