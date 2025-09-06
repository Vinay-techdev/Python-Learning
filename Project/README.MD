# 🤖 Jarvis – Python Voice Assistant  

Jarvis is a simple **voice-controlled assistant** built in Python.  
It can recognize your voice, respond with speech, open websites, play music, and even fetch live news.  

---

## 🚀 Features  

✅ **Speech Recognition** – Understands voice commands using Google Speech API  
✅ **Text-to-Speech** – Responds with a natural voice using `pyttsx3`  
✅ **Web Automation** – Opens Google, YouTube, LinkedIn in your browser  
✅ **Music Playback** – Plays songs from a custom `musicLibrary`  
✅ **News Fetching** – Reads out the latest headlines using NewsAPI  
✅ **Wake Word Detection** – Responds when you say *“Jarvis”*  

---

## 📂 Project Structure  

```

Jarvis/
├── jarvis.py         # Main code
├── musicLibrary.py   # Dictionary of songs with links
├── .env              # Store your API key here
├── requirements.txt  # Required dependencies
└── README.md         # Project documentation

````

---

## 🔧 Setup & Installation  

### 1️⃣ Clone this repository  
```bash
git clone https://github.com/Vinay-techdev/Python-Learning.git
cd Python-Learning/Jarvis
````

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Add your NewsAPI key

Create a `.env` file inside the `Jarvis/` folder:

```
API_KEY=your_newsapi_key_here
```

Get your free API key from 👉 [https://newsapi.org](https://newsapi.org).

### 4️⃣ Run Jarvis

```bash
python jarvis.py
```

---

## 🎙️ Example Commands

* "Jarvis, open Google" → Opens Google in browser
* "Jarvis, open YouTube" → Opens YouTube
* "Jarvis, play Namo Namo" → Plays a song (if available in `musicLibrary.py`)
* "Jarvis, news" → Reads top BBC News headlines

---

## 📦 Requirements

* Python 3.8+
* `speechrecognition`
* `pyttsx3`
* `requests`
* `python-dotenv`

*(already listed in `requirements.txt`)*

---

## 🚀 Future Improvements

* Add weather updates 🌦️
* Integrate with ChatGPT for smart replies 💬
* Control system apps (open Notepad, Calculator, etc.)

---

## 🧑‍💻 Author

👋 Made with Python by **Vinay**
🔗 [LinkedIn](https://www.linkedin.com/in/vinay-techdev) | [GitHub](https://github.com/Vinay-techdev)

---

⭐ If you like this project, don’t forget to **star the repo**!

```
---