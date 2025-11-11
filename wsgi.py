from app import app
from src.utility.weather_summary import WeatherSummaryPredictor
from src.utility.precip_type_predicting import PrecipTypePredictor
from src.utility.temperature_prediction import TemperaturePredictor

try:
    app.predictors = {
        'summary': WeatherSummaryPredictor(),
        'precip': PrecipTypePredictor(),
        'temp': TemperaturePredictor()
    }
    app.logger.info("All prediction models loaded successfully for production.")
except Exception as e:
    app.logger.critical(f"Failed to load models on startup: {e}")
    raise
