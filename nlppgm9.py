# TEXTBLOB AND SENTIMENTAL ANALYSIS

from textblob import TextBlob

para="Kaiser claims to be committed to human rights, but many would argue her career at Cambridge Analytica tells a different story. She has worked extensively for the firm, pitching business to clients in countries that have a history of exploitation by western political mercenaries, including Lithuania, Benin, Ethiopia and Libya."

x=TextBlob(para)

print(x.tags)

# Sentimental Analysis

print(x.sentiment.polarity)
# -1 = Negative sentence
# 0 = Neutal sentence
# +1 = Postive sentence
