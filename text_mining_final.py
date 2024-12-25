import nltk
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk import ngrams
import string

# Example text input
txt = 'The Disease was NOT cured yet. It now is cured. In conclusion, it is cured.'  # Example text
txt = txt.lower()

# Remove punctuation
translator = str.maketrans('', '', string.punctuation)
txt_cleaned = txt.translate(translator)

# Tokenize text
tokenized_sentence = word_tokenize(txt_cleaned)

print("Tokenized Sentence:", tokenized_sentence, '\n')

# Stemming example
words = ["cure", "cured", "curing", "cures"]
ps = PorterStemmer()

print("Stemmed Words:")
for word in words:
    print(f"{word}: {ps.stem(word)}")
print('\n')

# Generate bigrams and trigrams
n_gram_size = 2  # Set to 2 for bigrams, 3 for trigrams
n_grams = list(ngrams(tokenized_sentence, n_gram_size))

print(f"{n_gram_size}-grams:")
for gram in n_grams:
    print(gram)
print('\n')

# Count occurrences of "is cured" and "not cured"
is_cured_count = n_grams.count(('is', 'cured'))
not_cured_count = n_grams.count(('not', 'cured'))

# Results
print(f"The phrase 'is cured' appears {is_cured_count} time(s).")
print(f"The phrase 'not cured' appears {not_cured_count} time(s).")

# Final decision
print("\nResults:")
if is_cured_count > not_cured_count:
    print("The Disease is cured.")
else:
    print("The Disease is NOT cured.")