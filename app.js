document.getElementById('file-upload').addEventListener('change', handleFileUpload);
document.getElementById('detect-btn').addEventListener('click', sendToModel);

function handleFileUpload(event) {
   const file = event.target.files[0];
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
   // Placeholder function to connect to your model later
   alert("Send image to the model here!");
}
