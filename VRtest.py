import speech_recognition as sr
from textblob import TextBlob
from playsound import playsound
from gtts import gTTS

GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""
"""

counter = 0

def speaker(toTalk):
    tts = gTTS(toTalk)
    tts.save('speaking' + str(counter) + '.mp3')
    playsound('speaking' + str(counter) + '.mp3')
speaker("good morning, tell me about your day")
# obtain audio from the microphone

def listener():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening")
        audio = r.listen(source)
    try:
        speech = r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS)
        return speech
    except sr.UnknownValueError:
        print("Google Cloud Speech could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Cloud Speech service; {0}".format(e))
        print("You said: " + speech)
speech = listener()


blob = TextBlob(speech)
for sentence in blob.sentences:
    print(sentence.sentiment.polarity)
    happyness = sentence.sentiment.polarity
if happyness > 0:
    counter +=1
    speaker("Seems like your day has been pretty good! Keep it up!")
else:
    counter +=2
    speaker("Cheer up, its not too bad. There's always tomorrow!")
