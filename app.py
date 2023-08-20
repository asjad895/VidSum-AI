from flask import Flask, render_template, request, redirect, url_for,send_from_directory
from VidSumAI.components.video_subtitle import SubtitleGenerator,video2usbConfig
from VidSumAI.components.video_summarizer import Summarizer
from VidSumAI.components.video_downloader import VideoDownloader
from VidSumAI.pipeline import run_training_pipeline
import threading
from gtts import gTTS

import os

app = Flask(__name__)
app.config['upload_dir']=os.path.join('uploads/')
os.makedirs(app.config['uploads/'],exist_ok=True)
print("Loading Model:  ")
summarizer=Summarizer()
summarizer.load_model()



@app.route('/')
def index():
    return render_template('index.html')


# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Handle uploaded file or video link here
        file = request.files.get('file')
        video_link = request.form.get('video-link')

        # Process the file or video link
        # ... (your processing code here)
        # Process the file or video link and generate transcription and summary data
        transcription_data = "Generated transcription data"
        summary_data = "Generated summary data"

        return render_template('index.html', transcription_data=transcription_data, summary_data=summary_data)

        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
