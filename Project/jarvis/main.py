import speech_recognition as sr
import pyttsx3
import webbrowser
import musicLibrary
import requests
from dotenv import load_dotenv
import os
import time

load_dotenv()
API_KEY = os.getenv("API_KEY")

# Initialize recognizer and engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(command):
    command = command.lower()
    if "open google" in command:
        webbrowser.open("https://google.com")
    elif "open linkedin" in command:
        webbrowser.open("https://linkedin.com")
    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
    elif command.lower().startswith("play"):
        song = command[5:].strip()
        link = musicLibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak("Song not found.")
    elif "headlines" in command.lower():
        res = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}")
        
        if res.status_code == 200:
            data = res.json()
            articles = data.get("articles", [])
            if not articles:
                speak("No news found.")
            else:
                speak("Here are the top news headlines from India.")
                for article in articles[:5]:  # top 5 headlines
                    title = article.get("title")
                    if title:
                        print(title)  # optional: print to console
                        speak(title)
        else:
            speak("Failed to fetch news.")
            print("News API Error:", res.text)

# Main loop
if __name__ == "__main__":
    speak("Initializing Jarvis....")
    
    while True:
        print("Listening for wake word...")
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=4)

            word = recognizer.recognize_google(audio).lower()
            
            # Wake word detection
            if word in ["jarvis", "jarivs"]:
                speak("Yah")  # Jarvis responds immediately
                print("Wake word detected. Listening for command...")

                # Listen for the actual command
                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                    try:
                        command = recognizer.recognize_google(audio)
                        print(f"Command: {command}")
                        processCommand(command)
                    except sr.UnknownValueError:
                        speak("Sorry, I did not get that.")
            
            time.sleep(0.5)  # prevent rapid looping

        except sr.WaitTimeoutError:
            print("No speech detected, retrying...")
        except sr.UnknownValueError:
            print("Could not understand audio")
        except Exception as e:
            print(f"Error: {e}")
