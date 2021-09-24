# LEMMATIZATION

import nltk
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize('eating'))

print(lemmatizer.lemmatize('books'))
