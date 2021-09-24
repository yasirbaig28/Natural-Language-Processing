# Tokenization

from nltk.tokenize import sent_tokenize, word_tokenize

text= 'Kaiser claims to be committed to human rights, but many would argue her career at Cambridge Analytica tells a different story. She has worked extensively for the firm, pitching business to clients in countries that have a history of exploitation by western political mercenaries, including Lithuania, Benin, Ethiopia and Libya.'

s=sent_tokenize(text)

print(s)
print(type(s))
print(len(s))

#convert everything to individual words

words=word_tokenize(text)
#print(words)

#for i in words:
    #print(i) #it will print everything separately

#To remove any special character in the text
#for i in words:
    #if i in "!@#$%^&*()><.,":
        #del i
#print(words)
