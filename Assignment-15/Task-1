import requests
import json

def get_weather(city):
    api_key = "d0d9c29cd5e0f6aa41e9370ad3874404"  # your working key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    try:
        # timeout avoids hanging forever
        response = requests.get(url, timeout=5)

        # If HTTP code is not 200 -> API error
        if response.status_code != 200:
            print("Error: Could not connect to API. Check your API key or city name.")
            return

        weather_data = response.json()

        print("\nWeather Details (JSON):")
        print(json.dumps(weather_data, indent=4))

    except requests.exceptions.Timeout:
        print("Error: Request timed out. Please check your network connection.")

    except requests.exceptions.ConnectionError:
        print("Error: Unable to connect to the internet or API server.")

    except Exception as e:
        print(f"Unexpected Error: {e}")


# --------- MAIN PROGRAM ---------
city = input("Enter city name: ")
get_weather(city)
