import requests
import json
import os

def get_weather_and_store(city_name):
    api_key = input("Enter your OpenWeatherMap API key: ").strip()  # Ask user for API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    try:
        # Make the API request
        response = requests.get(base_url, params={"q": city_name, "appid": api_key, "units": "metric"})
        
        # Raise exception if response code is not 200
        response.raise_for_status()
        
        data = response.json()
        
        # Extract necessary details
        weather_info = {
            "city": data["name"],
            "temp": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "weather": data["weather"][0]["description"].capitalize()
        }

        # Print formatted JSON output
        print(json.dumps(weather_info, indent=4))

        # Store results in local file (append if file exists)
        file_path = "results.json"
        if os.path.exists(file_path):
            with open(file_path, "r+", encoding="utf-8") as f:
                try:
                    existing_data = json.load(f)
                    if not isinstance(existing_data, list):
                        existing_data = []
                except json.JSONDecodeError:
                    existing_data = []
                existing_data.append(weather_info)
                f.seek(0)
                json.dump(existing_data, f, indent=4)
        else:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump([weather_info], f, indent=4)

    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 401:
            print("Error: Invalid API key.")
        elif response.status_code == 404:
            print(f"Error: City '{city_name}' not found.")
        else:
            print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("Error: Network connection issue.")
    except Exception as err:
        print(f"An unexpected error occurred: {err}")

# Example usage
city = input("Enter city name: ")
get_weather_and_store(city)
