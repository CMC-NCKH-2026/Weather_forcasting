import joblib
import pandas as pd
import numpy as np
import os

class PrecipTypePredictor:
    def __init__(self, model_path=None):
        if model_path is None:
            # Get the absolute path to the models directory
            current_dir = os.path.dirname(os.path.abspath(__file__))
            project_root = os.path.dirname(os.path.dirname(current_dir))
            model_path = os.path.join(project_root, 'models', 'preciptype_forecast_model.joblib')
        
        # Load model + label encoder
        data = joblib.load(model_path)
        self.model = data['model']
        self.label_encoder = data['label_encoder']

    def predict(self, input_data):
        """
        Predict precipitation type based on input data.
        
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
            }

        Returns:
            str: Predicted precipitation type
        """
        # Create DataFrame from input data
        new_df = pd.DataFrame([input_data])

        # Add cyclical features
        new_df['hour_sin'] = np.sin(2 * np.pi * new_df['Hour'] / 24.0)
        new_df['hour_cos'] = np.cos(2 * np.pi * new_df['Hour'] / 24.0)
        new_df['month_sin'] = np.sin(2 * np.pi * new_df['Month'] / 12.0)
        new_df['month_cos'] = np.cos(2 * np.pi * new_df['Month'] / 12.0)

        # Remove the Hour and Month column, as the models aren't trained with that
        # inplace so it won't create a new object every call
        new_df.drop(['Hour', 'Month'], axis=1, inplace=True)

        # Make prediction (encoded)
        pred_encoded = self.model.predict(new_df)

        # Convert back to original label
        pred_label = self.label_encoder.inverse_transform(pred_encoded)
        return pred_label[0]




        
