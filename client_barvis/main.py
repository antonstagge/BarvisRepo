# -*- coding: utf-8 -*-

import requests
import os
from threading import Thread
import website
import ai_request
import speech_recognition
import json

recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source1:
    recognizer.adjust_for_ambient_noise(source1)


def startWebsite():
    website.run()


def speak(text):
    newText = text.encode("utf-8")
    os.system("say " + newText)


def listen(timeout):
    with speech_recognition.Microphone() as source:
        print "listening"
        try:
            audio = recognizer.listen(source, timeout=timeout)
        except speech_recognition.WaitTimeoutError as e:
            audio = None
    print "done listening"
    if audio is not None:
        try:
            # return recognizer.recognize_sphinx(audio)
            return recognizer.recognize_google(audio, language="sv-SE")
        except speech_recognition.UnknownValueError:
            print("Could not understand audio")
        except speech_recognition.RequestError as e:
            print("Recog Error; {0}".format(e))
    return ""


def waitForBarvis():
    while True:
        prompt = listen(1)
        words = prompt.split(' ')
        barvis = False
        for word in words:
            if word == "barbies" or word == "Barbies":
                barvis = True
        if barvis:
            speak("Vad vill du?")
            command = listen(5)
            if command == "":
                continue
            print command
            response = ai_request.aiQurey(command)
            print response
            jsonRespone = json.loads(response)
            action = jsonRespone["result"]["action"]
            print action
            if action == "fromTo":
                speak("From To action")
            else:
                speak("Jag kan inte hjälpa dig med det.")



websiteThread = Thread(target=startWebsite)
websiteThread.start()
waitForBarvis()

#websiteThread.join()
