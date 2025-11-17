import joblib
import pandas as pd
import numpy as np
import os

class TemperaturePredictor:
    def __init__(self, model_path=None):
        if model_path is None:
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

            example:
            {
                'Temperature (C)': 15.2,             
                'Apparent Temperature (C)': 14.8,   
                'Humidity': 0.80,
                'Wind Speed (km/h)': 12.5,
                'Wind Bearing (degrees)': 220.0,
                'Visibility (km)': 9.5,
                'Pressure (millibars)': 1014.0,
                'Hour': 14,  # 2 PM
                'Month': 11, # November
                'Summary': 'Overcast',
                'Precip Type': 'rain'
            }

        Returns:
            float: Predicted temperature for the next hour
        """
        # create DataFrame from input data
        new_df = pd.DataFrame([input_data])
        
        # add cyclical features
        new_df['hour_sin'] = np.sin(2 * np.pi * new_df['Hour'] / 24.0)
        new_df['hour_cos'] = np.cos(2 * np.pi * new_df['Hour'] / 24.0)
        new_df['month_sin'] = np.sin(2 * np.pi * new_df['Month'] / 12.0)
        new_df['month_cos'] = np.cos(2 * np.pi * new_df['Month'] / 12.0)
        
        # make prediction
        prediction = self.model.predict(new_df)
        return prediction[0]