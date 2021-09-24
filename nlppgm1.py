#Implementing Tokenization-BPE

# [1] Reading Corpus

import pandas as pd

text=pd.read_csv("sample.txt",header=None)

corpus=[]
for row in text.values:
    tokens = row[0].split("")
    for token in tokens:
        corpus.append(token)

# [2] Text Preparation

vocab=list(set("".join(corpus)))
vocab.remove('')

corpus=["".join(token)for token in corpus]

corpus=[token+'</w>'for token in corpus]

# [3] Learning BPE

import collections
corpus= collections.Counter(corpus)

corpus=dict(corpus)
print("Corpus:",corpus)
