# STEMMING 

from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
#or
#from nltk import pos_tag
text= 'Kaiser claims to be committed to human rights, but many would argue her career at Cambridge Analytica tells a different story. She has worked extensively for the firm, pitching business to clients in countries that have a history of exploitation by western political mercenaries, including Lithuania, Benin, Ethiopia and Libya.'

sentence=sent_tokenize(text)

words=word_tokenize(text)
#print(len(words))
print(words)

#To print root-words of the text
from nltk.stem.porter import PorterStemmer

stemmed=[PorterStemmer().stem(w)for w in words]

print(stemmed)

print(nltk.pos_tag(stemmed))#Fetch us the parts-of-Speech
#print(pos_tag(stemmed))
