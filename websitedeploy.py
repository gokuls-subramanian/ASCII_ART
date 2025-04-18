from flask import Flask, Response
import time
import os

app = Flask(__name__)

def load_ascii_frames(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    return content.split('\n\n')

@app.route('/')
def home():
    return "Welcome to ASCII Live Server! Try /sigmamale or /gigachad"

@app.route('/<name>')
def stream_ascii(name):
    options = {
        'sigmamale': 'Asciiarts/sigmamale.txt',
        'gigachad': 'Asciiarts/Gigachad.txt',
        'andrewtate': 'Asciiarts/Andrewtate.txt',
        'trollface': 'Asciiarts/Trollface.txt',
    }

    if name not in options:
        return f"No such animation: {name}", 404

    frames = load_ascii_frames(options[name])

    def generate():
        while True:
            for frame in frames:
                yield f"\033[H{frame}"
                time.sleep(0.1)

    return Response(generate(), mimetype='text/plain')

# ✅ ADD THIS:
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
