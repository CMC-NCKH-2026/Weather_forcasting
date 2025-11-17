from app import app
from src.utility.weather_summary import WeatherSummaryPredictor
from src.utility.precip_type_predicting import PrecipTypePredictor
from src.utility.temperature_prediction import TemperaturePredictor

# bootstrap the model objects in memory for wsgi, prevents the models from being loaded multiple times in memory
# note: this should NOT be run while developmental work, this wont start the server!
try:
    app.predictors = {
        'summary': WeatherSummaryPredictor(),
        'precip': PrecipTypePredictor(),
        'temp': TemperaturePredictor()
    }
except Exception as e:
    app.logger.critical(f"Failed to load models on startup: {e}")
    raise