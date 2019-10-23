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
from random import randint

import webbrowser
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

DIALOGFLOW_PROJECT_ID = 'virtualrealityassistant-uqfhte'
DIALOGFLOW_LANGUAGE_CODE = 'en-US'
GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""{
  "type": "service_account",
  "project_id": "virtualrealityassistant-uqfhte",
  "private_key_id": "cffce866c0b12d418064a07049d6a16b15b9ca9e",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC3qZv/hVT/mVTo\npDV6EospgzOlp5oTl3pI3z/KycyCVmc/IOHZLfC75tdzIPK1gMBKdPoP/VrNhELf\nbBEDsxgQk6yZ9db+WSezUryBBZpcG1X/iBCaV4oJE6FR7cv3LjfnKLppVP1Ue9Sj\n+p1gfVImxthFi9ynQIZ96sq/OIB+f4TrsoWf6HxsNfwyazuUb76oRAy+NT9dM7uS\nhjbKJaI16Ag8B4XZw3kws5btf030yGp1yeuUJiRPCKjI0YkwT/29sAgT/5GfBiB3\nid5hvgW4ibW3+U10VgbanZB75NTKrqemd5I7ApphhWVCMF7IW85euxHAiRWB0kiT\nhkLt6zVdAgMBAAECggEAF+tdvv1HKOO4EHVkZpHYMG+fMBWgJimN+kQjC37VJOtq\nVmkqqM2IIvypNhwGKBfM01WhRKhXJVlymST6oUv3mB8XdVS0a5tCZaMinD4V0KWZ\nwWYf3W4FsvFsyt4IuJg7HR6rinDQbmqTMsj+qpSfuJ+ghow00E6BxY/o2FccOv0Z\nRUalbpcb3YMDQszsAsoOEp4Zbg0SfeR6PfE24bZIjHilVEgu9Vez/7NHtl8/+rE2\nuAm3SBjIVdmAMhRXEoakmedEsxQ2mpZDcCf0U7a8E3XYU8tPD8rS40urzWpUNmu1\nyTEsbqPtwVOOLbXLqnVgy98uJZvDuoFv3OBpBHF2QQKBgQDylVidthwfBR+tvkXB\nuhhKODtXbqVY4Wcg4JcvzYoXiOsY9EXF2EBluXO/OqmJx/Fl3e4DPJGWadorqKIU\nBr7OXY84sQENBSdNrhTyrH4snr224raib0eoXPDNZMAsEEsgU6vOVqnK7u9ebwrw\nnkDidVflZPRiAhQeJcIPTwWywQKBgQDB0gX+V1Uc68naWvn/uLPDY8TkXZ8TXLCM\njj42/FUrcIIeRj/RyoeOqoHK+hPhGvsK4l0+c21XEjLrPluHOOrPAXkstx7UigII\n48OX9Esb/MXzXxcjHBgp++/t1fD/1gW7xQLy9ujPpmAGDU+5fCSWMsvugq4DS6O7\nChVG0DLVnQKBgA5di77jLu0jV4npb6YWSCP1CoaV9dK6nmnTAwEAsgHMyOdUZ+Fc\negvMHK+hYLLZFVGL//FPH+wBXrshJF/9OkVsQvP/f2lu+bHe8jygvGQWDnQLHvel\nkV/GCTiQk9TILjq+2bjBZxKubZxxBPvU01DV1Buwi8xWBSz33XMcoeDBAoGBAInk\nhEMZmwJCdo+VHjvjCnG+b3wRZ3V9AlZddMHl8CpBlzE2xXzaXGsRv9nK5Y3HhkeO\nGMyvjmDeH7/h03h29AdmgvFfLt4DecMdWDCpqy40PhkR1AI0oLRt+5r4FMfPWrDm\nT1zQcX4aXkKwAcJzIgyCAzijXG4XyFrvp4eD5Ea5AoGAbbM++n53SDFMyWqONLOx\nQFcdIHa/dcazQa69cKMCFtYIxDFGcTyTqgO+Y/u3xb+aEonGqV7w2phSExznObnB\nJIAN6kmtjW3wcxldDeOIiOD6F4exaUi8TvOOMqsueFJBTumjSySvudH0thLwFZl5\nmPCicU4VdJRiquM3QAHqZv0=\n-----END PRIVATE KEY-----\n",
  "client_email": "cady-35@virtualrealityassistant-uqfhte.iam.gserviceaccount.com",
  "client_id": "101376967158060634515",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/cady-35%40virtualrealityassistant-uqfhte.iam.gserviceaccount.com"
}"""


counter = 0

def speaker(toTalk):
    rand = randint(0,100)
    tts = gTTS(toTalk)
    tts.save('speaking' + str(rand) + '.mp3')
    playsound('speaking' + str(rand) + '.mp3')
    # os.remove('speaking' + str(counter) + '.mp3')

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
        listener()
    except sr.RequestError as e:
        print("Could not request results from Google Cloud Speech service; {0}".format(e))
        listener()


def youtube():
    searchQuery = listener()
    browser = webdriver.Chrome(r"C:\Users\Bhou5\Downloads\chromedriver_win32\chromedriver.exe")
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
