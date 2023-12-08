import speech_recognition as sr
import pyttsx3
import pywhatkit as wk
import datetime
import wikipedia
import webbrowser
import os
import random
import cv2
import pyautogui
import datetime
import operator
import requests
import sys


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning!")

    elif hour >= 12 and hour < 18:
        speak("good afternoon!")

    else:
        speak("good evening!")

    speak("ready to comply. what can I do for you ?")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("say that again please...")
        return 'none'
    return query


if __name__ == "__main__":
    wishMe()

    while True:
        query = takecommand().lower()
        if 'jarvis' in query:
            print("yes sir")
            speak("yes sir")

        elif 'what is' in query:
            speak("searching wikipedia...")
            query = query.replace("what is", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'just open google' in query:
            webbrowser.open("google.com")

        elif 'open google' in query:
            speak("what should I search ?")
            qry = takecommand().lower()
            webbrowser.open(f'{qry}')
            results = wikipedia.summary(qry, sentences=1)
            speak(results)

        elif 'just open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open youtube' in query:
            speak("what you will like to watch ?")
            qry = takecommand().lower()
            wk.playonyt(f'{qry}')

        elif 'search on youtube' in query:
            query = query.replace("search on youtube", "")
            webbrowser.open(f"www.youtube.com/results?search-query={query}")

        elif 'open command prompt' in query:
            os.system("start cmd")

        elif 'open camera' in query:
            cap=cv2.VideoCapture(0)
            while True:
                ret,img=cap.read()
                cv2.imshow('webcam',img)
                k=cv2.waitkey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyallwindows()

        elif 'time' in query:
            Time = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"sir, the time is {Time}")

        elif 'date' in query:
             date  = datetime.datetime.now().strftime('%D:%M:%Y')
             speak(f"sir, the date is {date}")

        elif 'shut down the system' in query:
             os.system(("shutdown /s /t 5"))


        elif 'go to sleep' in query:
             speak('alright then, I am switching off')
             sys.exit()

