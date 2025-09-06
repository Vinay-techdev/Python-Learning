import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommond(c):
    if "open google" in c.lower():
      webbrowser.open("https://google.com")
    elif "open linkedin" in c.lower():
      webbrowser.open("https://linkedin.com")
    elif "open youtube" in c.lower():
      webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
       webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
       song = c.lower().split(" ")[1]
       link = musicLibrary.music[song]
       webbrowser.open(link)
    elif "news" in c.lower():
       res = requests.get(f"https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={API_KEY}")
       if res.status_code == 200:
          data = res.json()
          
          # Extract the article in link
          articles = data.get('articles', [])

          for article in articles:
             speak(article['title'])
       

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
      r = sr.Recognizer()

      print("recognizing...")
      try:
        # Listing for the "Jarvis" word and obtain audio from the microphone
        with sr.Microphone() as source:
          r.adjust_for_ambient_noise(source, duration=0.5)
          print("Listening...")
          audio = r.listen(source, timeout=5, phrase_time_limit=4)

        word = r.recognize_google(audio)

        if word.lower() in ["jarvis", "jarivs"]:
           speak("yah")

           # Listen for commond
           with sr.Microphone() as source:
              print("Jarivs active..")
              audio = r.listen(source)
              commond = r.recognize_google(audio)

              processCommond(commond)
      except Exception as e:
        print("Error; {0}".format(e))