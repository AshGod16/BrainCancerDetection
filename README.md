# 🧠 Brain Cancer Detection System

## 🔍 Overview
This project implements a deep learning-based system for detecting and classifying brain cancer from medical imaging data. It utilizes ResNet and U-Net architectures to provide both classification and segmentation capabilities for medical professionals.

## 📁 Project Structure
```
BRAINCANCERDETECTION/
├── server/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── api.py              # API endpoints and routing
│   │   ├── image_processing.py # Image preprocessing functions
│   │   ├── model_loading.py    # Model management utilities
│   │   └── utilities.py        # Helper functions
│   ├── models/
│   │   ├── classifier-resnet-model.json
│   │   ├── ResUNet-model.json
│   │   ├── __init__.py
│   │   └── server.py
│   └── static/
│       ├── css/
│       │   └── style.css
│       ├── js/
│       │   └── app.js
│       └── templates/
│           └── index.html
```

## ⭐ Features
- 🔍 Automated brain tumor detection and classification
- 🎯 Medical image segmentation for tumor region identification
- 🖥️ Web-based user interface for image upload and analysis
- 🔌 RESTful API for integration with other medical systems
- ⚡ Real-time processing and results visualization

## 🛠️ Technologies Used
- **Backend**: Python, Flask
- **Deep Learning**: ResNet (Classification), U-Net (Segmentation)
- **Frontend**: HTML5, CSS3, JavaScript
- **Image Processing**: OpenCV, PIL
- **Model Serving**: TensorFlow/PyTorch (depending on your implementation)

## 💻 Installation

### 📋 Prerequisites
- Python 3.8+
- Virtual environment (recommended)
- GPU support (optional but recommended for faster processing)

### 🚀 Setup Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/braincancerdetection.git
   cd braincancerdetection
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Download pre-trained models:
   - Place the ResNet classifier model in `server/models/`
   - Place the U-Net segmentation model in `server/models/`

5. Start the server:
   ```bash
   python server/models/server.py
   ```

## 📱 Usage

### 🌐 Web Interface
1. Access the web interface at `http://localhost:5000`
2. Upload a brain MRI image through the interface
3. Wait for the processing to complete
4. View the detection results and segmentation overlay

### 🔗 API Endpoints
- `POST /api/predict`
  - Upload an image for cancer detection
  - Returns classification results

## 🤖 Model Information
- **Classification Model**: ResNet-based architecture trained on brain MRI datasets
- **Segmentation Model**: Modified U-Net architecture for precise tumor boundary detection
- Both models are pre-trained on extensive medical imaging datasets

## 👩‍💻 Development

### 🆕 Adding New Features
1. Create a new branch for your feature
2. Implement the feature following the project's coding standards
3. Write appropriate tests
4. Submit a pull request

## 🤝 Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

---
⚠️ **Note**: This project is intended for research and educational purposes only. It should not be used as the sole diagnostic tool for medical decisions. Always consult with qualified medical professionals for patient diagnosis and treatment.