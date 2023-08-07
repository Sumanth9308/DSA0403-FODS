import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import matplotlib.pyplot as plt

nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text):

    text = text.lower()
  
    text = text.translate(str.maketrans('', '', string.punctuation))
   
    tokens = word_tokenize(text)
   
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    return filtered_tokens

def calculate_frequency_distribution(tokens):
    return nltk.FreqDist(tokens)

def plot_frequency_distribution(freq_dist, n):
    freq_dist.plot(n, cumulative=False)

def main():
    data = pd.read_csv('data.csv')

    preprocessed_text = data['feedback'].apply(preprocess_text)

    all_tokens = [token for tokens in preprocessed_text for token in tokens]

    freq_dist = calculate_frequency_distribution(all_tokens)

    try:
        n = int(input("Enter the number of top words to display: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    print(f"Top {n} most frequent words:")
    for word, frequency in freq_dist.most_common(n):
        print(f"{word}: {frequency}")

    plot_frequency_distribution(freq_dist, n)
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title(f'Top {n} Most Frequent Words')
    plt.show()

if __name__ == "__main__":
    main()
