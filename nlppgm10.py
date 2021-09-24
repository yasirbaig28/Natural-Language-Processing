# Correcting sentences using TEXTBLOB 

from textblob import TextBlob

para="I havv good speling mistask"

x=TextBlob(para)

print(x.correct())
