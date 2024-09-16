import joblib
import os
import numpy as np
from sklearn.exceptions import NotFittedError

# Get the absolute path to the trained model file
model_path = os.path.join(os.path.dirname(__file__), '../model/trained_model.sav')

# Load the trained model with error handling
try:
    model = joblib.load(model_path)
    print("Model loaded successfully!")
except FileNotFoundError:
    print(f"Error: Model file not found at {model_path}.")
    model = None
except Exception as e:
    print(f"Error loading the model: {e}")
    model = None

def predict_diabetes(input_data):
    """Predict whether a person has diabetes based on the input data."""
    if model is None:
        raise Exception("Model is not loaded. Cannot make predictions.")
    
    try:
        # Ensure the input data is a numpy array
        input_data = np.array(input_data).reshape(1, -1)
        
        # Make prediction
        prediction = model.predict(input_data)[0]
        
        return prediction
    
    except NotFittedError:
        raise Exception("The model is not properly trained or fitted.")
    
    except ValueError as e:
        raise Exception(f"Input data is invalid: {e}")
    
    except Exception as e:
        raise Exception(f"An error occurred during prediction: {e}")
