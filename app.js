document.getElementById('file-upload').addEventListener('change', handleFileUpload);
document.getElementById('detect-btn').addEventListener('click', sendToModel);

function handleFileUpload(event) {
   const file = event.target.files[0];
   console.log(file);
   const reader = new FileReader();
   reader.onload = function(e) {
      const img = new Image();
      img.onload = function() {
         const canvas = document.getElementById('output-canvas');
         const ctx = canvas.getContext('2d');
         canvas.width = img.width;
         canvas.height = img.height;
         ctx.drawImage(img, 0, 0);
      };
      img.src = e.target.result;
   };
   reader.readAsDataURL(file);
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
        console.error("Error processing image:", result.error);
    }
 }