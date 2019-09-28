from textblob import TextBlob
import time
print("Say anything... A N Y T H I N G...")
text = input()
blob = TextBlob(text)
for sentence in blob.sentences:
    print(sentence.sentiment.polarity)
    happyness = sentence.sentiment.polarity
if happyness > 0:
    print("Seems like your writing is pretty happy to me")
else:
    print("Cheer up fam, its not too bad")
