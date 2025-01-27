import os
import datetime
import webbrowser
import wikipedia
import pyttsx3 as pts
import speech_recognition as sr

os.system("cls")

nama = "blue"

engine = pts.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wisme():
    hour = int(datetime.datetime.now().hour)
    
    if hour >= 0 and hour < 12:
        speak("Good Morning" + nama)
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon" + nama)
    else:
        speak("Good Night" + nama)

def takecommend():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-us")
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        query = None
    except sr.RequestError as e:
        print(f"Say that again please; {e}")
        query = None
    return query

speak(f"Hello my name is {nama} i can help you")
wisme()
query = takecommend()

if "wikipedia" in query.lower():
    speak("searching wikipedia")
    query = query.replace("wikipedia","")
    results = wikipedia.summary(query,sentences=2)
    print(results)
    speak(results)
elif f"open youtube {nama}" in query.lower():
    speak("Loading Yutube")
    url = "https://www.youtube.com"
    webbrowser.open(url)
    chrume_path = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    webbrowser.get(chrume_path).open(url)