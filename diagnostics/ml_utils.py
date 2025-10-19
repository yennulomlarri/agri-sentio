import tensorflow as tf
import numpy as np
from PIL import Image
import io
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'ml_models', 'crop_disease_model.h5')

# Load model once on startup
model = tf.keras.models.load_model(MODEL_PATH)

CLASS_NAMES = ['Healthy', 'Blight', 'Rust', 'Mildew']

def predict_disease(image_bytes):
    """
    Run inference and return prediction + confidence
    """
    img = Image.open(io.BytesIO(image_bytes)).resize((224, 224))
    img_array = np.expand_dims(np.array(img) / 255.0, axis=0)
    preds = model.predict(img_array)
    confidence = float(np.max(preds))
    label = CLASS_NAMES[np.argmax(preds)]
    return {"label": label, "confidence": confidence}
