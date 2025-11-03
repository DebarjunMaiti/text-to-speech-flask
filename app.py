from flask import Flask, render_template, request, jsonify, send_file
from gtts import gTTS
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/speak', methods=['POST'])
def speak():
    text = request.form['text']
    if not text.strip():
        return jsonify({"error": "No text provided"}), 400

    filename = f"output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp3"
    output_path = os.path.join("static", filename)

    # Use gTTS (auto language detection, works with Hindi + English)
    tts = gTTS(text=text, lang='hi', slow=False, tld='co.in')
    tts.save(output_path)

    return jsonify({"audio_url": f"/static/{filename}"})

@app.route('/download/<filename>')
def download_audio(filename):
    path = os.path.join("static", filename)
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    os.makedirs("static", exist_ok=True)
    app.run(debug=True)
