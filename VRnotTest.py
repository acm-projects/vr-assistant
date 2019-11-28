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

import re
import time
import datetime
from random import randint

import webbrowser
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

DIALOGFLOW_PROJECT_ID = #INSERT YOUR DIALOGFLOW PROJECT ID HERE
DIALOGFLOW_LANGUAGE_CODE = 'en-US'
GOOGLE_CLOUD_SPEECH_CREDENTIALS = #INSERT YOUR GOOGLE CLOUD CREDENTIALS HERE


counter = 0

def speaker(toTalk):
    rand = randint(0,100)
    tts = gTTS(toTalk)
    tts.save('speaking' + str(rand) + '.mp3')
    playsound('speaking' + str(rand) + '.mp3')


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
        listener()
    except sr.RequestError as e:
        print("Could not request results from Google Cloud Speech service; {0}".format(e))
        listener()


def youtube():
    searchQuery = listener()
    browser = webdriver.Chrome(#INSERT THE PATH TO YOUR CHROME DRIVER HERE)
    browser.get('https://www.youtube.com')
    browser.find_element_by_id("content").click()
    browser.find_element_by_xpath(r'//*[@id="search"]').send_keys(searchQuery + Keys.ENTER)
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="title-wrapper"]').click()

def meditation():
    minutes = re.findall(r"\d+", response.query_result.fulfillment_text)
    print(minutes[0])
    seconds = int(minutes[0]) * 60
    print("meditating for " + str(seconds))

    filename = 'meditation.mp3'
    webbrowser.open(filename)

    time.sleep(seconds)
    os.system("taskkill /im Music.UI.exe /f")
    return 0

SESSION_ID = 'current-user-id'
endConversation = ""

speaker("Hello. I'm Mischa, your personal assistant. How are you feeling today?")
content = listener()
print("You said: " + content)
speech = content
client = language.LanguageServiceClient()
document = types.Document(
    content=content,
    type=enums.Document.Type.PLAIN_TEXT)
annotations = client.analyze_sentiment(document=document)
magnitude = annotations.document_sentiment.magnitude
file = open("SentimentLog.txt", "a")
file.write("\n")
file.write(str(datetime.datetime.now()))
file.write("\n")
file.write(str(magnitude))
file.close()
print(magnitude)
speaker("Okay, your daily sentiment has been logged. What can I do for you today?")

#This checks to see if the conversation should continue
while endConversation != "Goodbye":

    content = listener()
    print("You said: " + content)
    speech = content
    client = language.LanguageServiceClient()
    document = types.Document(
        content=content,
        type=enums.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(document=document)
    magnitude = annotations.document_sentiment.magnitude
    print(magnitude)

    #Code to determine intent
    text_to_be_analyzed = speech
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
    text_input = dialogflow.types.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.types.QueryInput(text=text_input)
    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
    except InvalidArgument:
        raise
    print("Query text:", response.query_result.query_text)
    print("Detected intent:", response.query_result.intent.display_name)
    endConversation = str(response.query_result.intent.display_name)
    print("Detected intent confidence:", response.query_result.intent_detection_confidence)
    print("Fulfillment text:", response.query_result.fulfillment_text)
    counter +=1
    speaker(response.query_result.fulfillment_text)

    #parse intent for time if meditation
    if response.query_result.intent.display_name == "Meditation":
        meditation()
    if response.query_result.intent.display_name == "Music":
        speaker("What would you like to listen to?")
        counter +=1
        youtube()
