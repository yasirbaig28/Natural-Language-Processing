# SnowballStemmer

import nltk
from nltk.stem import SnowballStemmer
print(SnowballStemmer.languages)

French_stemmer = SnowballStemmer('french')
print(French_stemmer.stem('Bonjoura'))

