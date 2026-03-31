import streamlit as st
import tensorflow as tf
import numpy as np

# Tensorflow Model Prediction
def model_prediction(test_image):
    model = tf.keras.models.load_model(r"D:\\Shalviii\\2 month project\\Plant disease detection\\trained_model.keras")
    image = tf.keras.preprocessing.image.load_img(test_image, target_size=(128, 128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])  # Convert single image to a batch
    prediction = model.predict(input_arr)
    result_index = np.argmax(prediction)
    return result_index

# Disease class names
class_name = [
    'Apple___Apple_scab',
    'Apple___Black_rot', 
    'Apple___Cedar_apple_rust', 
    'Apple___healthy',
    'Blueberry___healthy', 
    'Cherry_(including_sour)___Powdery_mildew', 
    'Cherry_(including_sour)___healthy',
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 
    'Corn_(maize)___Common_rust_',
    'Corn_(maize)___Northern_Leaf_Blight', 
    'Corn_(maize)___healthy', 
    'Grape___Black_rot',
    'Grape___Esca_(Black_Measles)', 
    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 
    'Grape___healthy',
    'Orange___Haunglongbing_(Citrus_greening)', 
    'Peach___Bacterial_spot', 
    'Peach___healthy',
    'Pepper,_bell___Bacterial_spot', 
    'Pepper,_bell___healthy', 
    'Potato___Early_blight', 
    'Potato___Late_blight',
    'Potato___healthy', 
    'Raspberry___healthy', 
    'Soybean___healthy', 
    'Squash___Powdery_mildew',
    'Strawberry___Leaf_scorch', 
    'Strawberry___healthy', 
    'Tomato___Bacterial_spot', 
    'Tomato___Early_blight',
    'Tomato___Late_blight', 
    'Tomato___Leaf_Mold', 
    'Tomato___Septoria_leaf_spot',
    'Tomato___Spider_mites Two-spotted_spider_mite', 
    'Tomato___Target_Spot',
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 
    'Tomato___Tomato_mosaic_virus', 
    'Tomato___healthy'
]

# Load full disease information with Fertilizer, Care, Symptoms, Prevention
from plant_disease_data import disease_info

# Streamlit Sidebar
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select Page", ["Home", "About", "Disease Recognition"])

# Home Page
if app_mode == "Home":
    st.header("PLANT DISEASE RECOGNITION SYSTEM")
    st.image("home_page.jpeg", use_container_width=True)
    st.markdown("""
    Welcome to the Plant Disease Recognition System! 

    Upload a plant image to detect diseases and get recommendations!

    ### How It Works
    1. Upload an image on the Disease Recognition page.
    2. Our model will detect any disease.
    3. You’ll get recommendations for fertilizer, care, symptoms, and prevention.

    ### Why Use This?
    - Accurate model predictions
    - Useful care and fertilizer guidance
    - Easy to use and fast!
    """)

elif app_mode == "About":
    st.header("About")
    st.markdown("""
    #### About Dataset:
   This dataset is recreated using offline augmentation from the original dataset.This dataset consists of about 87k rgb images of healthy and diseased crop leaves which is categorized into 38 different classes.The total dataset is divided into 80/20 ration of training and validation set preserving the directory structure.A new directory containing 33 test images is created later for prediction purpose.
    #### Content:
    - Train (70295 images)
    - Validation (17572 images)
    - Test (33 images)
    """)

elif app_mode == "Disease Recognition":
    st.header("Disease Recognition")
    test_image = st.file_uploader("Choose an Image:")

    if st.button("Show Image"):
        if test_image is not None:
            st.image(test_image, use_container_width=True)

    if st.button("Predict"):
        if test_image is not None:
            with st.spinner("Predicting..."):
                result_index = model_prediction(test_image)
                predicted_disease = class_name[result_index]
                st.success(f"Model is predicting: **{predicted_disease}**")

                info = disease_info.get(predicted_disease)
                if info:
                    st.markdown(f"### 🧪 Fertilizer Recommendation:\n{info['Fertilizer']}")
                    st.markdown(f"### 🌿 Care Tips:\n{info['Care']}")
                    if 'Symptoms' in info:
                        st.markdown(f"### ⚠️ Symptoms:\n{info['Symptoms']}")
                    if 'Prevention' in info:
                        st.markdown(f"### 🛡️ Preventive Measures:\n{info['Prevention']}")
                else:
                    st.warning("No detailed information available for this disease yet.")
        else:
            st.error("Please upload an image first.")
