// Display a message when the file input changes
const fileInput = document.querySelector('input[type="file"]');
fileInput.addEventListener('change', () => {
    const fileName = fileInput.files[0].name;
    alert(`Selected file: ${fileName}`);
});
