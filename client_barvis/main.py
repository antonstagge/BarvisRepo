# -*- coding: utf-8 -*-

import requests
import os
from threading import Thread
import website
import speech_recognition

recognizer = speech_recognition.Recognizer()

def startWebsite():
    website.run()

def speak(text):
    os.system("say " + text)

def listen():
    with speech_recognition.Microphone() as source:
        #recognizer.adjust_for_ambient_noise(source)
        print "listening"
        audio = recognizer.listen(source)
    print "done listening"
    try:
        #return recognizer.recognize_sphinx(audio)
        return recognizer.recognize_google(audio, language="sv-SE")
    except speech_recognition.UnknownValueError:
        print("Could not understand audio")
    except speech_recognition.RequestError as e:
        print("Recog Error; {0}".format(e))

    return ""

def waitForBarvis():
    while True:
        prompt = listen()
        words = prompt.split(' ')
        barvis = False
        for word in words:
            if word == "barbies" or word == "Barbies":
                barvis = True
        if barvis:
            speak("Vad vill du?")
            command = listen()
            speak("Okej jag: " + command)
            speak("Beep boop beep... Resultatet blev att du e keff")



websiteThread = Thread(target=startWebsite)
websiteThread.start()
waitForBarvis()

#websiteThread.join()
