# STEMMING v/s EMMATIZATION

import nltk

from nltk.stem import PorterStemmer
word_stemmer = PorterStemmer()
print(word_stemmer.stem('believes'))

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize('believes'))
