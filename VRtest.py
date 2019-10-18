import speech_recognition as sr
from textblob import TextBlob
from playsound import playsound
from gtts import gTTS

import argparse

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

import dialogflow
from google.api_core.exceptions import InvalidArgument

import os

DIALOGFLOW_PROJECT_ID = 'virtualrealityassistant-uqfhte'
DIALOGFLOW_LANGUAGE_CODE = 'en-US'
GOOGLE_CLOUD_SPEECH_CREDENTIALS =

def speaker(toTalk):
    tts = gTTS(toTalk)
    tts.save('speaking.mp3')
    playsound('speaking.mp3')
    os.remove("speaking.mp3")

speaker("Hello world.")
speaker("My name is cady")
speaker("I am here to listen")
speaker("Tell me about your feelings ")
#obtain audio from the microphone

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


SESSION_ID = 'current-user-id'
endConversation = ""

#requires
def meditation():
    speaker("How long would you like to meditate for?")
    meditateLength = listener()
    playsound("meditation.mp3", False)
    time.sleep(meditateLength * 60)
    return 0


def intentIdentifier(intent):
    if intent == "Meditation":
        meditation()
    if intent == "Goodbye":
        return 0

#This determines intent and then sends the variables
def intentListener():
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

    #Code to determine intent
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
    text_input = dialogflow.types.TextInput(text=speech, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.types.QueryInput(text=text_input)
    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
    except InvalidArgument:
        raise
    print("Query text:", response.query_result.query_text)
    print("Detected intent:", response.query_result.intent.display_name)
    intentName = str(response.query_result.intent.display_name)
    print("Detected intent confidence:", response.query_result.intent_detection_confidence)
    print("Fulfillment text:", response.query_result.fulfillment_text)
    intentIdentifier(intentName)
    speaker(response.query_result.fulfillment_text)
intentListener()

#for manual intents (non-spoken) : will be used for sentiment analysis responses
#0001 triggers the happy intent
#0002 triggers the sad intent
def manualIntent(speech):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
    text_input = dialogflow.types.TextInput(text=speech, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.types.QueryInput(text=text_input)
    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
    except InvalidArgument:
        raise
    print("Query text:", response.query_result.query_text)
    print("Detected intent:", response.query_result.intent.display_name)
    intentName = str(response.query_result.intent.display_name)
    print("Detected intent confidence:", response.query_result.intent_detection_confidence)
    print("Fulfillment text:", response.query_result.fulfillment_text)
    intentIdentifier(intentName)
    speaker(response.query_result.fulfillment_text)
