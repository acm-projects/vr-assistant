#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import speech_recognition as sr
from playsound import playsound
from gtts import gTTS

import time

GOOGLE_CLOUD_SPEECH_CREDENTIALS = 
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

searchQuery = listener()
browser = webdriver.Chrome(r"C:\Users\Bhou5\Downloads\chromedriver_win32\chromedriver.exe")
browser.get('https://www.youtube.com')
browser.find_element_by_id("content").click()
browser.find_element_by_xpath(r'//*[@id="search"]').send_keys(searchQuery + Keys.ENTER)
time.sleep(1)
browser.find_element_by_xpath('//*[@id="title-wrapper"]').click()
