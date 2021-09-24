# Translating sentences using TEXTBLOB 

from textblob import TextBlob

para="My name is Peter Parker"

x=TextBlob(para)

print(x.translate(to='hi'))
print(x.detect_language())
