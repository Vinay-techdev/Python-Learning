import pyjokes
import pyttsx3

# Printing Jokes...
joke = pyjokes.get_joke()
print(joke)

# Text to Speech
engine = pyttsx3.init()
engine.say("Hey Coders, how are you doing")
engine.runAndWait()