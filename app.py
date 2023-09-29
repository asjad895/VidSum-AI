from flask import Flask, render_template, request, redirect, url_for,send_from_directory
# from VidSumAI.components.video_subtitle import SubtitleGenerator,video2usbConfig
# from VidSumAI.components.video_summarizer import Summarizer
from VidSumAI.components.video_downloader import VideoDownloader
# from VidSumAI.pipeline import run_training_pipeline
import threading
from gtts import gTTS

import os

app = Flask(__name__)
app.config['upload_dir']=os.path.join('uploads/')
os.makedirs(app.config['upload_dir'],exist_ok=True)
print("Loading Model:  ")
# summarizer=Summarizer()
# summarizer.load_model()



@app.route('/')
def index():
    """
    It renders the index.html file in the templates folder

    Returns:
      The index.html file is being returned.
    """
    return render_template('index.html')


# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    """
    The function upload_file() takes in a video file or a video link, transcribes the video, and
    summarizes the transcript

    Returns:
      the transcript and summary text.
    """
    if request.method == 'POST':
        video_file = request.files["file"]
        # subtitle_generator = SubtitleGenerator(config=video2usbConfig)
        if video_file:
            filename = video_file.filename
            video_path = os.path.join(os.path.join(
                app.config['upload_dir'], filename))
            print(video_path)
            video_file.save(video_path)
            task = 'transcribe'
            option = request.form.get('taskSelect')
            if option == 'Translate':
                task = 'Translate'
                print("translate task is selected:", task)
            # subtitle = subtitle_generator.get_subtitles(video_paths=video_path, model_path='tiny', task=task, verbose=False)
        else:
            video_link = request.form["video-link"]
            print(video_link)
            downloader = VideoDownloader(url=video_link, save_path=app.config['upload_dir'])
            video_path = downloader.download()
            print(video_path)
            task = 'Transcribe'
            option = request.form.get('taskSelect')
            print(option)
            if option == 'Translate':
                task = 'Translate'
                print("translate task is selected:", task)
            print("task selected:", task)
            # subtitle = subtitle_generator.get_subtitles(video_paths=[video_path],model_path='tiny', task=task, verbose=False)
        # transcript_text = subtitle[1]['text']
        # summary_text = summarizer.summarize_text(transcript_text)
        # tts = gTTS(summary_text, tld="co.uk")
        # audio_path = os.path.join(app.config['upload_dir'], 'summary.mp3')
        # tts.save(audio_path)
        transcription_data = "Generated transcription data"
        summary_data = "Generated summary data"

        return render_template('index.html', transcription_data=transcription_data, summary_data=summary_data)

@app.route('/audio/<path:filename>')
def serve_audio(filename):
    return send_from_directory(app.config['upload_dir'], filename, mimetype='audio/mpeg')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
