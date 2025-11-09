import joblib
import pandas as pd
import numpy as np
import os

class TemperaturePredictor:
    def __init__(self, model_path=None):
        if model_path is None:
            # Get the absolute path to the models directory
            current_dir = os.path.dirname(os.path.abspath(__file__))
            project_root = os.path.dirname(os.path.dirname(current_dir))
            model_path = os.path.join(project_root, 'models', 'temperature_forecast_model.joblib')
        self.model = joblib.load(model_path)

    def predict(self, input_data):
        """
        Predict temperature based on input data.
        
        Args:
            input_data (dict): Dictionary with keys matching the features.
                              Values should be scalars (not lists).
        
        Returns:
            float: Predicted temperature for the next hour
        """
        # Create DataFrame from input data
        new_df = pd.DataFrame([input_data])
        
        # Add cyclical features
        new_df['hour_sin'] = np.sin(2 * np.pi * new_df['Hour'] / 24.0)
        new_df['hour_cos'] = np.cos(2 * np.pi * new_df['Hour'] / 24.0)
        new_df['month_sin'] = np.sin(2 * np.pi * new_df['Month'] / 12.0)
        new_df['month_cos'] = np.cos(2 * np.pi * new_df['Month'] / 12.0)
        
        # Make prediction
        prediction = self.model.predict(new_df)
        return prediction[0]