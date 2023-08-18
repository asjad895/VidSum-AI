document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('upload-form');
    const fileInput = document.getElementById('file-upload');
    const fileNameDisplay = document.getElementById('file-name');
    const linkInput = document.getElementById('video-link');
    fileInput.addEventListener('change', function() {
        if (fileInput.files.length > 0) {
            fileNameDisplay.textContent = 'Selected: ' + fileInput.files[0].name;
        } else {
            fileNameDisplay.textContent = '';
        }
    });

    form.addEventListener('submit', function(event) {
        if (!fileInput.files.length && !linkInput.value.trim()) {
            event.preventDefault();
            alert('Please select a file or enter a video link.');
        }
    });
});


