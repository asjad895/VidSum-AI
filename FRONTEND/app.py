from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            file.save(os.path.join('uploads', file.filename))
            return redirect(url_for('index'))
    return render_template('upload.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Handle uploaded file or video link here
        file = request.files.get('file')
        video_link = request.form.get('video-link')

        # Process the file or video link
        # ... (your processing code here)

        return "Form submitted successfully"

if __name__ == '__main__':
    app.run(debug=True)
