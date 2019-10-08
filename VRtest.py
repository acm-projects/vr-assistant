import speech_recognition as sr
from playsound import playsound
from gtts import gTTS

import argparse

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

import random

GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""{
}
"""

counter = 0

def speaker(toTalk):
    tts = gTTS(toTalk)
    tts.save('speaking' + str(counter) + '.mp3')
    playsound('speaking' + str(counter) + '.mp3')

speaker("Hello world.")
counter+=1
speaker("My name is krishna")
counter+=1
speaker("I am here to listen")
counter+=1
speaker("Tell me about your feelings ")
counter+=1


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
        return 0
    except sr.RequestError as e:
        print("Could not request results from Google Cloud Speech service; {0}".format(e))





speech = listener()
print("You said: " + str(speech))

content = speech
client = language.LanguageServiceClient()
document = types.Document(
    content=content,
    type=enums.Document.Type.PLAIN_TEXT)
annotations = client.analyze_sentiment(document=document)
magnitude = annotations.document_sentiment.magnitude
print("On a scale of -1 to 1, the sentiment score of the spoken text is " + str(magnitude))


def verySad():
    sadfix = ["call your assigned contact?", "play some of your favorite music?", "start a meditation session?"]
    randomness = random.randint(0,2)
    speaker("I see that your day has not gone very well. Would you like me to " + sadfix[randomness])
    verySadresponse = listener()
    if verySadresponse == 0:
        speaker("Sorry, I didn't catch that, could you speak again?")
    if verySadresponse == "no" or verySadresponse == False:
        randomness += 1
        speaker("Maybe you would like me to " + sadfix[randomness])

def sentimentResponse(score):
    score = score *100;
    if score <-75:
        verySad()
    if -75 <= score < -20:
        verySad()        ##sad()
    else:
        verySad()
    # if -20<= score <= 20:
    #     indeterminant()
    # if 20 < score < 75:
    #     happy()
    # if 75 <= score < 100:
    #     veryHappy()

sentimentResponse(magnitude)
