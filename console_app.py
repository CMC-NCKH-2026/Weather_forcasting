from src.utility.weather_summary import WeatherSummaryPredictor
from src.utility.precip_type_predicting import PrecipTypePredictor
from src.utility.temperature_prediction import TemperaturePredictor


def get_weather_summary_input():
    """Gets user input for the WeatherSummaryPredictor."""
    print("\nEnter the required parameters for Weather Summary Prediction:")
    input_data = {
        'Temperature (C)': float(input("Temperature (C): ")),
        'Apparent Temperature (C)': float(input("Apparent Temperature (C): ")),
        'Humidity': float(input("Humidity: ")),
        'Wind Speed (km/h)': float(input("Wind Speed (km/h): ")),
        'Wind Bearing (degrees)': float(input("Wind Bearing (degrees): ")),
        'Visibility (km)': float(input("Visibility (km): ")),
        'Pressure (millibars)': float(input("Pressure (millibars): ")),
        'Hour': int(input("Hour (0-23): ")),
        'Month': int(input("Month (1-12): ")),
        'Precip Type': input("Precip Type (e.g., rain, snow): ")
    }
    return input_data


def get_precip_type_input():
    """Gets user input for the PrecipTypePredictor."""
    print("\nEnter the required parameters for Precipitation Type Prediction:")
    input_data = {
        'Temperature (C)': float(input("Temperature (C): ")),
        'Apparent Temperature (C)': float(input("Apparent Temperature (C): ")),
        'Humidity': float(input("Humidity: ")),
        'Wind Speed (km/h)': float(input("Wind Speed (km/h): ")),
        'Wind Bearing (degrees)': float(input("Wind Bearing (degrees): ")),
        'Visibility (km)': float(input("Visibility (km): ")),
        'Pressure (millibars)': float(input("Pressure (millibars): ")),
        'Hour': int(input("Hour (0-23): ")),
        'Month': int(input("Month (1-12): "))
    }
    return input_data


def get_temperature_input():
    """Gets user input for the TemperaturePredictor."""
    print("\nEnter the required parameters for Temperature Prediction:")
    input_data = {
        'Temperature (C)': float(input("Temperature (C): ")),
        'Apparent Temperature (C)': float(input("Apparent Temperature (C): ")),
        'Humidity': float(input("Humidity: ")),
        'Wind Speed (km/h)': float(input("Wind Speed (km/h): ")),
        'Wind Bearing (degrees)': float(input("Wind Bearing (degrees): ")),
        'Visibility (km)': float(input("Visibility (km): ")),
        'Pressure (millibars)': float(input("Pressure (millibars): ")),
        'Hour': int(input("Hour (0-23): ")),
        'Month': int(input("Month (1-12): ")),
        'Summary': input("Summary (e.g., Overcast, Clear): "),
        'Precip Type': input("Precip Type (e.g., rain, snow): ")
    }
    return input_data


def main():
    """Main function to run the console application."""
    while True:
        print("\nChoose a model to use:")
        print("1. Weather Summary Predictor")
        print("2. Precipitation Type Predictor")
        print("3. Temperature Predictor")
        print("0. Exit")

        choice = input("Enter your choice (0-3): ")

        if choice == '1':
            try:
                input_data = get_weather_summary_input()
                predictor = WeatherSummaryPredictor()
                result = predictor.predict(input_data)
                print(f"\nPredicted Weather Summary: {result}")
            except (ValueError, KeyError) as e:
                print(f"Invalid input: {e}")

        elif choice == '2':
            try:
                input_data = get_precip_type_input()
                predictor = PrecipTypePredictor()
                result = predictor.predict(input_data)
                print(f"\nPredicted Precipitation Type: {result}")
            except (ValueError, KeyError) as e:
                print(f"Invalid input: {e}")

        elif choice == '3':
            try:
                input_data = get_temperature_input()
                predictor = TemperaturePredictor()
                result = predictor.predict(input_data)
                print(f"\nPredicted Temperature: {result:.2f} C")
            except (ValueError, KeyError) as e:
                print(f"Invalid input: {e}")

        elif choice == '0':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()