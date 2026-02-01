# 😴 Drowsiness Detection using YOLO26

A real-time drowsiness detection system built with YOLO26 that can help prevent accidents by detecting driver drowsiness through webcam monitoring.

## 🎯 Overview

This project implements a complete pipeline for building a custom drowsiness detection model using YOLO26. The system captures facial data through a webcam, trains a deep learning model to detect signs of drowsiness, and performs real-time detection to alert when drowsiness is detected.

## ✨ Features

- **Custom Data Collection**: Capture your own training data using webcam
- **Easy Annotation**: Integration with MakeSense.ai for labeling
- **YOLO26 Training**: Train state-of-the-art object detection model
- **Real-time Detection**: Monitor drowsiness in real-time via webcam
- **Sample Predictions**: Test model on sample images

## 📁 Project Structure

```
Drowsiness-detection/
├── sample_data/           # Sample images for testing
├── collect_data.py        # Script for capturing training data via webcam
├── training.ipynb         # Jupyter notebook for training YOLOv26 model
├── predict.ipynb          # Jupyter notebook for predictions
├── dataset.yaml           # Dataset configuration for YOLO
├── requirements.txt       # Python dependencies
└── .gitignore            # Git ignore file
```

## 🛠️ Requirements

- Python 3.8+
- Webcam (for data collection and real-time detection)
- GPU (recommended for training)

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/KhwaishK/Drowsiness-detection.git
   cd Drowsiness-detection
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

### 1. Data Collection

Run the data collection script to capture images using your webcam:

```bash
python collect_data.py
```

**What it does:**
- Opens your webcam
- Captures images for different classes ("awake", "drowsy")
- Saves images in organized class folders

### 2. Data Labeling

After collecting data, label your images using MakeSense.ai:

1. Go to [MakeSense.ai](https://www.makesense.ai/)
2. Upload your collected images
3. Create labels ("awake", "drowsy")
4. Draw bounding boxes around the face
5. Export annotations in YOLO format
6. Place the exported labels in the appropriate folders

**Expected folder structure after labeling:**
```
data/
├── images/
│   ├── train/
│   └── val/
└── labels/
    ├── train/
    └── val/
```

### 3. Model Training

Open and run the training notebook:

```bash
jupyter notebook training.ipynb
```

**Training parameters you can adjust:**
- `epochs`: Number of training iterations (default: 50-100)
- `batch_size`: Number of images per batch (default: 16)
- `img_size`: Input image size (default: 640)
- `learning_rate`: Model learning rate

### 4. Prediction

After training, use the prediction notebook to test your model:

```bash
jupyter notebook predict.ipynb
```

**The notebook provides:**
- **Real-time detection**: Detect drowsiness through webcam feed
- **Sample image prediction**: Test on the two sample images in `sample_data/` folder
- Visualization of detection results with bounding boxes and confidence scores
