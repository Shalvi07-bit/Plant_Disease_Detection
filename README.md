# 🌿 Plant Disease Detection System (CNN-Based)

## 📌 Overview

This project is a **Deep Learning-based Plant Disease Detection System** that uses a **Convolutional Neural Network (CNN)** model to classify plant diseases from leaf images.

Additionally, a **hybrid CNN + XGBoost approach** is explored to improve prediction performance and model interpretability.

The system also provides:

* 🧪 Fertilizer recommendations
* 🌿 Care tips
* ⚠️ Symptoms
* 🛡️ Prevention methods

The application is deployed using **Streamlit** for real-time predictions.

---
## 🚀 Features

* 🌱 Image-based disease classification using CNN
* 🧠 Hybrid CNN + XGBoost model (advanced approach)
* 📊 38 plant disease classes
* 🧪 Fertilizer & care recommendations
* 💻 Interactive Streamlit web app
* ⚡ Real-time prediction

---
## 🧠 Model Details

### 🔹 CNN Model

* Used Convolutional Neural Networks for feature extraction
* Automatically learns patterns from leaf images
* Input Size: 128 × 128 images

### 🔹 Hybrid Model (CNN + XGBoost)

* CNN used for feature extraction
* XGBoost used as a classifier on extracted features
* Improves performance and robustness

### 📊 Performance

* Accuracy: **~97.6%**
* Validation Accuracy: **~95%**

---

## 📊 Dataset

This project uses the **PlantVillage Dataset** from Kaggle.

* Total Images: ~87,000
* Classes: 38 plant diseases
* Type: RGB leaf images

🔗 Dataset Link: https://www.kaggle.com/datasets/emmarex/plantdisease

---
## 📂 Project Structure

Plant_Disease_Detection/
│── main.py
│── plant_disease_data.py
│── trained_model.keras
│── training_hist.json
│── requirements.txt
│── README.md
│── notebooks/
```

---

## ⚙️ Installation & Setup

```bash id="t5n2qs"
git clone https://github.com/your-username/Plant_Disease_Detection.git
cd Plant_Disease_Detection
pip install -r requirements.txt
streamlit run main.py
```

---

## 💻 How It Works

1. Upload plant leaf image
2. CNN model extracts features
3. Model predicts disease class
4. System displays:

   * Disease name
   * Fertilizer recommendation
   * Care tips
   * Symptoms
   * Prevention

---

## 📈 Model Performance Insights

* Training accuracy improves consistently
* Validation accuracy stabilizes around ~95%
* Loss decreases over epochs indicating good learning

---

## 🔮 Future Enhancements

* 📱 Mobile app deployment
* 🌍 Real-time camera detection
* 📊 Explainable AI (SHAP integration)
* 🌾 Expansion to more crops

---
## ⭐ Key Highlight

✔ CNN-based deep learning model
✔ Hybrid ML approach (CNN + XGBoost)
✔ End-to-end pipeline from image to recommendation

