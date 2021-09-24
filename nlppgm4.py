# RegularExpressionStemmer

import nltk
from nltk.stem import RegexpStemmer
Reg_stemmer = RegexpStemmer('ing')
print(Reg_stemmer.stem('ingeat'))
