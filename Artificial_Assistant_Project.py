#ARTIFICIAL ASSISTANT PROJECT BY YASH AGARWAL
#KIPM-COLLEGE OF ENGINEERING AND TECHNOLOGY, GIDA, GORAKHPUR
#UNDER THE GUIDANCE OF AMIT SIR (CETPA)

#IMPORT FILES

import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import os
import sys
import random

#VOICE ENGINE

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
#print(voices[0])

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#WISH ME FUNCTION

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning Mr. Yash")
    elif hour>=12 and hour<18:
        speak("Good afternoon Mr. Yash")
    else:
        speak("Good evening Mr. Yash")
    speak("This is Artificial Assistant Sir. How I can help you?")

#RECOGNIZE THE VOICE 

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold=1
        #r.energy_threshold=500
        #r.dynamic_energy_threshold=True
        audio=r.listen(source)
    try:
        print('Recognizing...')
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print("Sorry, I can't hear you! Please repeat again...")
        speak("Sorry, I can't hear you! Please repeat again...")
        return 'None'
    return query

#COMMANDS TO BE PERFORMED BY ARTIFICIAL HUMAN

if __name__=="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace('wikipedia','')
            results=wikipedia.summary(query,sentences=2)
            speak('According to wikipedia')
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'play music' in query:
            music_dir = 'F://music_dir'
            songs = os.listdir(music_dir)
            x=len(songs)-1
            z=random.randint(0,x)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[z]))
        elif 'thank you' in query:
            speak("Thanks for using me Mr. Yash")
            sys.exit()
