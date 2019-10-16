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

GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""{
  "type": "service_account",
  "project_id": "vr-assistant-utgani",
  "private_key_id": "9dcec1ee91f640fb4e73b38b1719ef3b4835a968",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCvmmhNH37cKrU1\njQrLfBIBuFCLieoHFY4X0/b0AO766ymlVjL9qBMiHOSqK+CWqTUYA2oVS2XPZ/2T\nZS8UqNS6I5jisvDUQuB6/cIEWkzlT30v92ja0h6TASesYZLI5QNG03G7eou7uPul\nMZTTT0CLRGDb61k//L+qzZMrj9S7nA/ha5lRV5O8vVn24B1GlvEsEPFwvGsBbhOe\n8Y6SHZVHGUtxLlCQe9c5rzhmuV/fkcnWU9ZoszwvefrXLJf1wppO/yf5Izvh1J8J\nf3dHjs9qEU64h4uo/ht0bW8Bmv3nQW52r0v5xAl3cpuftp9NTXsu4dH+hs5ETS3N\n3QKBRLD1AgMBAAECggEACujNVQlBYN04X8jQ5F5jYf745gpd4y3II5vUCkmqjyUf\n87kcttyDv8lKvXW3YLTHayP/Ka6C9zUvMEKHf8GTYbMHcwIJ6y3yc0GjlZCkmVRs\nYxf8SCfopVpbhB6Vt2xe3T4SoUKWPsXZwGQJqm0QhfZsDA2dgFer8qkN3RV08mi/\nxiMoAo+Rq08qCUkMdU+KoE0qy+Wo/cS3QCAN1VbaJgOQlYhwl8FNLeMyWZg/+P4p\nQUi5+xaFtBrKrcGUmF6t+1RRKNN6+joY1so9yhZBQmpb/0x1mqNWkL3knAUdV+bH\nzAOV5P5lyymFJskjhawLtGoprpBnB0cZKbYZI0OViwKBgQDeP5AA53/mbKB28lEt\na9M2Q8+A0bBMLwhzmcQqB2FvS8NqM6QbKVUeySNeGpdbUUrEIT+k8T7aEPgpqIz+\nn9sWVQhCUhMiWnUOPst8YWEtl2zEr/HIjVXZ0LMx6hmES2iEZXHOrOggcaeC084b\nkuQdVlw8X3zIASDEns0eZHaeGwKBgQDKRWcju7PCorYH/fuCNR4WRq1UQpc9orlP\n3Pr3/joG7e3wg1y9xNfgw0SBPxx6/8KnDQMjHHD4OlR/QGasjB4h+8ThPgUDsqCb\nVKXsGkSvlPw5swt46HrQzasgVNvWKU+MjVVjW9439bVyoJGBkiKbd4MoXBothGZC\ntzQuGEueLwKBgB1jVk1oTzdPAeD4pddVvLYePWARWjiYt4tht9i+5RlscUinz3lv\n+7t4aV7WMVF37GUG6H2NEPyQ5d/MU+iPhs7rK45pf/I49+WMVCf8UHdQ4KcZhOU6\nGzIUML3W8MzXk9h9+ZCUuJUhsj7Qdx6aS+O9ObEaB0wDKiwVu5XbPvwlAoGARAB7\nQV8seyYazqsLsGXNPK38PdS5ZgZcCMaBNXip54R8NxzixAX2keD0GgOuvodX2LOe\nN2KrdDigCbwMCLx+sOwk75jbNLgMGMynj63xI5qSBY/1LmvyRlquyorc8a4nyVgG\nugW7utKHcwcahBYuPlg6pwn33w+hFZLkHw8Z9Q8CgYB8oTvVqEePkVRbRkMv6xrW\nmC91IHQ+VTL/w+T6Bf9prpHm7x4yvpXFRlIn0h0GQ9ZkKtBeAteoS4Q6DJR66KOZ\ngiu5rPsCOZQp0seLQEIq5Sdhh2Vb5E23RaPG9SBCWvEV0rwnEvgKid7nlXyeTHGP\n2n4RcJkqa8lBPSkj6XkSjA==\n-----END PRIVATE KEY-----\n",
  "client_email": "assistant@vr-assistant-utgani.iam.gserviceaccount.com",
  "client_id": "110596710906701922987",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/assistant%40vr-assistant-utgani.iam.gserviceaccount.com"
}
"""
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
