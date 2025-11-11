import os
from flask import Flask, render_template, request, redirect, url_for, g
import logging
import argparse

from src.utility.weather_summary import WeatherSummaryPredictor
from src.utility.precip_type_predicting import PrecipTypePredictor
from src.utility.temperature_prediction import TemperaturePredictor

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

try:
    predictors = {
        'summary': WeatherSummaryPredictor(),
        'precip': PrecipTypePredictor(),
        'temp': TemperaturePredictor()
    }
    app.logger.info("All prediction models loaded successfully.")
except Exception as e:
    app.logger.critical(f"Failed to load models on startup: {e}")


@app.route('/')
def index():
    mode = request.args.get('mode', 'summary')
    result = request.args.get('result', None)
    error = request.args.get('error', None)
    form_data = g.get('form_data', {})
    return render_template('index.html', mode=mode, result=result, error=error, form_data=form_data)


@app.route('/predict/summary', methods=['POST'])
def handle_summary_prediction():
    try:
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

        result = predictors['summary'].predict(input_data)

        return redirect(url_for('index', mode='summary', result=result))

    except (ValueError, KeyError):
        error_msg = "Invalid or missing input. Please check all fields are filled correctly."
        app.logger.warn(f"Value/KeyError in summary prediction: {error_msg}")
        return render_template('index.html', mode='summary', error=error_msg, form_data=request.form)

    except Exception as e:
        app.logger.error(f"Unhandled exception in summary prediction: {e}", exc_info=True)
        error_msg = "An unexpected error occurred. Please try again later."
        return render_template('index.html', mode='summary', error=error_msg, form_data=request.form)


@app.route('/predict/precip', methods=['POST'])
def handle_precip_prediction():
    try:
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

        result = predictors['precip'].predict(input_data)
        return redirect(url_for('index', mode='precip', result=result))

    except (ValueError, KeyError):
        error_msg = "Invalid or missing input. Please check all fields are filled correctly."
        app.logger.warn(f"Value/KeyError in precip prediction: {error_msg}")
        return render_template('index.html', mode='precip', error=error_msg, form_data=request.form)

    except Exception as e:
        app.logger.error(f"Unhandled exception in precip prediction: {e}", exc_info=True)
        error_msg = "An unexpected error occurred. Please try again later."
        return render_template('index.html', mode='precip', error=error_msg, form_data=request.form)


@app.route('/predict/temp', methods=['POST'])
def handle_temp_prediction():
    try:
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

        result_num = predictors['temp'].predict(input_data)
        result = f"{result_num:.2f} C"  # Formatting is good
        return redirect(url_for('index', mode='temp', result=result))

    except (ValueError, KeyError):
        error_msg = "Invalid or missing input. Please check all fields are filled correctly."
        app.logger.warn(f"Value/KeyError in temp prediction: {error_msg}")
        return render_template('index.html', mode='temp', error=error_msg, form_data=request.form)

    except Exception as e:
        app.logger.error(f"Unhandled exception in temp prediction: {e}", exc_info=True)
        error_msg = "An unexpected error occurred. Please try again later."
        return render_template('index.html', mode='temp', error=error_msg, form_data=request.form)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run the Weather Prediction App.")

    parser.add_argument(
        '-p', '--port',
        type=int,
        default=3636,
        help='Port number to run the application on (default: 3636)'
    )

    args = parser.parse_args()

    if not os.path.exists('templates'):
        os.makedirs('templates')

    app.logger.info(f"Starting server on host 0.0.0.0 and port {args.port}...")
    app.run(host='0.0.0.0', port=args.port, debug=False)