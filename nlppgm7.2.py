# Tokenization stopwords removal
#Stopwords are the words which have no actual meaning. 

from nltk.tokenize import sent_tokenize, word_tokenize

text= 'Kaiser claims to be committed to human rights, but many would argue her career at Cambridge Analytica tells a different story. She has worked extensively for the firm, pitching business to clients in countries that have a history of exploitation by western political mercenaries, including Lithuania, Benin, Ethiopia and Libya.'

sentence=sent_tokenize(text)
words=word_tokenize(text)
print(len(words))
print(words)

from nltk.corpus import stopwords
#print(stopwords.words("english"))
words=[ w for w in words if w not in stopwords.words("english")] #to remove the stopwords from the text above
print(len(words))
print(words)
