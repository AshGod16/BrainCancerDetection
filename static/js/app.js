document.getElementById('file-upload').addEventListener('change', handleFileUpload);
document.getElementById('detect-btn').addEventListener('click', sendToModel);

function handleFileUpload(event) {
    const file = event.target.files[0];
    console.log(file);
    if (!file) return;

    const reader = new FileReader();
    reader.onload = function (e) {
        const buffer = e.target.result;
        const tiff = new Tiff({ buffer });
        const canvas = tiff.toCanvas();
        
        // Convert canvas to a Data URL and set it as the src of the img tag
        const imgElement = document.getElementById('image');
        imgElement.src = canvas.toDataURL('image/png');  // or 'image/jpeg'
    };
    reader.readAsArrayBuffer(file);
}

async function sendToModel() {
    const fileInput = document.getElementById('file-upload');
    const file = fileInput.files[0];
    console.log(file);
    const formData = new FormData();
    formData.append('image', file);
 
    const response = await fetch('http://127.0.0.1:5000/api/predict', {
       method: 'POST',
       body: formData
    });
    
    const result = await response.json();
    if (result.processedImage) {
        // Display the processed image below the original image
        const processedImageElement = document.getElementById('processed-image');
        processedImageElement.src = result.processedImage; // Set the source to the processed image
        processedImageElement.style.display = 'block'; // Make it visible
    } else {
        console.log("Error processing image:", result.error);
    }
 }