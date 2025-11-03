# 🎤 Text-to-Speech Web Application (Multilingual)

A multilingual **Text-to-Speech (TTS)** web app built using **Flask** and **gTTS**.  
This application allows users to type text in **English, Hindi, or mixed (Hinglish)**,  
and the system will convert it into **natural-sounding speech** — with an option to **download the audio**.

---

## 🌟 Features

✅ Convert typed text into speech (supports multilingual text)  
✅ Works for English, Hindi, and mixed sentences (e.g., “Hello कैसे हो?”)  
✅ Simple and clean web UI built with HTML, CSS & JS  
✅ Built using Flask (Python backend)  
✅ Option to **play** or **download** generated audio  
✅ Self-contained — no external APIs needed  

---

## 🏗️ Project Structure
text-to-speech-app/ <br>
│<br>
├── app.py # Flask backend<br>
├── requirements.txt # Python dependencies<br>
├── README.md # Project documentation<br>
├── .gitignore # Ignored files for Git<br>
│<br>
├── templates/<br>
│ └── index.html # Frontend HTML page<br>
│<br>
├── static/<br>
    └── # Stores generated audio files<br>

---

## ⚙️ Installation Guide

Follow these steps to set up and run the project on your local machine 🧑‍💻

### 🪄 1. Clone the Repository
```bash
git clone https://github.com/DebarjunMaiti/text-to-speech-flask.git
cd text-to-speech-flask
```

🧱 2. Create a Virtual Environment: 

python -m venv venv

🔛 3. Activate the Virtual Environment:
On Windows (PowerShell):

venv\Scripts\activate

** If you get a permissions error, run:
Set-ExecutionPolicy Unrestricted -Scope Process

On macOS / Linux:

source venv/bin/activate

📦 4. Install Dependencies:

pip install -r requirements.txt

▶️ 5. Run the Flask Application

python app.py

You should see output like:
 * Running on http://127.0.0.1:5000
 * Debugger is active!

Then open your browser and visit:
👉 http://127.0.0.1:5000



🧠 Usage

1. Type a sentence in English, Hindi, or both (e.g., “Hello क्या हाल है”).
2. Click Speak to generate speech.
3. Click Download Audio to save the generated file locally.

🧩 Tech Stack

| Layer          | Technology Used                    |
| -------------- | ---------------------------------- |
| Frontend       | HTML, CSS, JavaScript              |
| Backend        | Flask (Python)                     |
| Text-to-Speech | gTTS (Google Text-to-Speech)       |
| Deployment     | Render / PythonAnywhere (optional) |

🚀 Deployment (Optional)
If you want to make this app live on the internet:

🥇 Deploy on Render
1. Go to Render
2. Click New → Web Service
3. Connect your GitHub repo
4. Set:
    Environment: python
    Build Command:
    pip install -r requirements.txt

    Start Command:
    python app.py

5. Deploy! 🎉
    Render will give you a public URL like:    
        https://text-to-speech-flask.onrender.com
        

📚 Example Sentences

Try these:
Hello कैसे हो?
आज weather बहुत अच्छा है!
Good morning सबको।
