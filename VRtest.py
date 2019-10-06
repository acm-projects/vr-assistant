import speech_recognition as sr
from textblob import TextBlob
from playsound import playsound
from gtts import gTTS

import argparse

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

GOOGLE_CLOUD_SPEECH_CREDENTIALS = 
counter = 0

def speaker(toTalk):
    tts = gTTS(toTalk)
    tts.save('speaking' + str(counter) + '.mp3')
    playsound('speaking' + str(counter) + '.mp3')

# speaker("Hello world.")
# counter+=1
# speaker("My name is hal9000")
# counter+=1
# speaker("I am here to listen")
# counter+=1
# speaker("Tell me about your feelings ")
# counter+=1
# obtain audio from the microphone

def listener():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening")
        audio = r.listen(source)
    try:
        print("speech detected")
        speech = r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS)
        return speech
    except sr.UnknownValueError:
        print("Google Cloud Speech could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Cloud Speech service; {0}".format(e))





speech = listener()
print("You said: " + speech)

content = speech
client = language.LanguageServiceClient()
document = types.Document(
    content=content,
    type=enums.Document.Type.PLAIN_TEXT)
annotations = client.analyze_sentiment(document=document)
magnitude = annotations.document_sentiment.magnitude
print(magnitude)


# blob = TextBlob(speech)
# for sentence in blob.sentences:
#     print(sentence.sentiment.polarity)
#     happyness = sentence.sentiment.polarity
# if happyness > 0:
#     counter +=1
#     speaker("Seems like your day has been pretty good! Keep it up!")
# else:
#     counter +=2
#     speaker("Cheer up, its not too bad. There's always tomorrow!")