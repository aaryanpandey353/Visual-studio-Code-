import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib

print("Initializing Jarvis")


MASTER = "Code With Aaryan"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def whishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour <12:
        speak("Good Morning" + MASTER)

    elif hour>=12 and hour <18:
        speak("Good Afternoon" + MASTER)

    else:
        speak("Good Evening" + MASTER)


    speak("I am Jarvis. How may I help you?")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
       print("listening...")
       audio = r.listen(source)

try:
        print
          
speak("Initializing Jarvis....")
whishMe()
