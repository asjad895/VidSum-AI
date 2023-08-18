
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('upload-form');
    const fileInput = document.getElementById('file-upload');
    const linkInput = document.getElementById('video-link');
    form.addEventListener('submit', function(event) {
        if (!fileInput.files.length && !linkInput.value.trim()) {
            event.preventDefault();
            alert('Please select a file or enter a video link.');
        }
    });
});




