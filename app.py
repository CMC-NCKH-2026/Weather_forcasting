import os
from flask import Flask, render_template, request, redirect, url_for, flash

from src.utility.weather_summary import WeatherSummaryPredictor
from src.utility.precip_type_predicting import PrecipTypePredictor
from src.utility.temperature_prediction import TemperaturePredictor
app = Flask(__name__)
# Set a secret key for flashing messages (good practice)
app.secret_key = os.urandom(24)


@app.route('/')
def index():
    """
    Renders the main page.
    'mode' determines which form to display (summary, precip, or temp).
    'result' or 'error' will be shown if they exist in the URL query.
    """
    mode = request.args.get('mode', 'summary')  # Default to 'summary'
    result = request.args.get('result', None)
    error = request.args.get('error', None)
    return render_template('index.html', mode=mode, result=result, error=error)


@app.route('/predict/summary', methods=['POST'])
def handle_summary_prediction():
    """Handles the form submission for Weather Summary."""
    try:
        # 1. Extract and type-cast all form data
        input_data = {
            'Temperature (C)': float(request.form['temp']),
            'Apparent Temperature (C)': float(request.form['apparent_temp']),
            'Humidity': float(request.form['humidity']),
            'Wind Speed (km/h)': float(request.form['wind_speed']),
            'Wind Bearing (degrees)': float(request.form['wind_bearing']),
            'Visibility (km)': float(request.form['visibility']),
            'Pressure (millibars)': float(request.form['pressure']),
            'Hour': int(request.form['hour']),
            'Month': int(request.form['month']),
            'Precip Type': request.form['precip_type']
        }

        # 2. Instantiate predictor and get result
        predictor = WeatherSummaryPredictor()
        result = predictor.predict(input_data)

        # 3. Redirect back to the index page to show the result
        return redirect(url_for('index', mode='summary', result=result))

    except ValueError:
        # Handle cases where user enters text instead of a number
        error_msg = "Invalid input. Please ensure all fields have the correct data type."
        return redirect(url_for('index', mode='summary', error=error_msg))
    except Exception as e:
        # Handle other potential model errors
        return redirect(url_for('index', mode='summary', error=str(e)))


@app.route('/predict/precip', methods=['POST'])
def handle_precip_prediction():
    """Handles the form submission for Precipitation Type."""
    try:
        # 1. Extract and type-cast all form data
        input_data = {
            'Temperature (C)': float(request.form['temp']),
            'Apparent Temperature (C)': float(request.form['apparent_temp']),
            'Humidity': float(request.form['humidity']),
            'Wind Speed (km/h)': float(request.form['wind_speed']),
            'Wind Bearing (degrees)': float(request.form['wind_bearing']),
            'Visibility (km)': float(request.form['visibility']),
            'Pressure (millibars)': float(request.form['pressure']),
            'Hour': int(request.form['hour']),
            'Month': int(request.form['month']),
        }

        # 2. Instantiate predictor and get result
        predictor = PrecipTypePredictor()
        result = predictor.predict(input_data)

        # 3. Redirect back to the index page
        return redirect(url_for('index', mode='precip', result=result))

    except ValueError:
        error_msg = "Invalid input. Please ensure all fields have the correct data type."
        return redirect(url_for('index', mode='precip', error=error_msg))
    except Exception as e:
        return redirect(url_for('index', mode='precip', error=str(e)))


@app.route('/predict/temp', methods=['POST'])
def handle_temp_prediction():
    """Handles the form submission for Temperature."""
    try:
        # 1. Extract and type-cast all form data
        input_data = {
            'Temperature (C)': float(request.form['temp']),
            'Apparent Temperature (C)': float(request.form['apparent_temp']),
            'Humidity': float(request.form['humidity']),
            'Wind Speed (km/h)': float(request.form['wind_speed']),
            'Wind Bearing (degrees)': float(request.form['wind_bearing']),
            'Visibility (km)': float(request.form['visibility']),
            'Pressure (millibars)': float(request.form['pressure']),
            'Hour': int(request.form['hour']),
            'Month': int(request.form['month']),
            'Summary': request.form['summary'],
            'Precip Type': request.form['precip_type']
        }

        # 2. Instantiate predictor and get result
        predictor = TemperaturePredictor()
        result_num = predictor.predict(input_data)
        result = f"{result_num:.2f} C"  # Format the result

        # 3. Redirect back to the index page
        return redirect(url_for('index', mode='temp', result=result))

    except ValueError:
        error_msg = "Invalid input. Please ensure all fields have the correct data type."
        return redirect(url_for('index', mode='temp', error=error_msg))
    except Exception as e:
        return redirect(url_for('index', mode='temp', error=str(e)))


if __name__ == '__main__':
    # Create the 'templates' directory if it doesn't exist
    if not os.path.exists('templates'):
        os.makedirs('templates')
    # Note: You would need to manually create the index.html file
    # in the 'templates' folder from the other file block.
    app.run(debug=True, host='0.0.0.0', port=5001)