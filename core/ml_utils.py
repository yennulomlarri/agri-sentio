import os
import numpy as np
from keras.models import load_model  
from keras.preprocessing import image  

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'crop_disease_model.h5')
_model = None

def load_crop_model():
    """Load and cache the crop disease detection model."""
    global _model
    if _model is None and os.path.exists(MODEL_PATH):
        _model = load_model(MODEL_PATH)
    return _model

def predict_disease(img_path):
    """
    Load the image, preprocess it, and return model prediction.
    Returns a dictionary with class and confidence.
    """
    model = load_crop_model()
    if model is None:
        return {"error": "Model not available or not loaded"}

    try:
        img = image.load_img(img_path, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0) / 255.0
        prediction = model.predict(img_array)
        predicted_class = int(np.argmax(prediction, axis=1)[0])
        confidence = float(np.max(prediction))
        return {"class": predicted_class, "confidence": round(confidence, 4)}
    except Exception as e:
        return {"error": str(e)}
