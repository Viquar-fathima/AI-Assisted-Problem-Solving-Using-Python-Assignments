import requests # type: ignore
import json
API_KEY = "7faac7ffaaf6687d935dbc1a59dd5a20"
def get_weather_with_errors(city):
    url = "http://api.openweathermap.org/data/2.5/weather?q=CITY_NAME&appid=7faac7ffaaf6687d935dbc1a59dd5a20&units=metric"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  
        data = response.json()

        print(json.dumps(data, indent=4))
        return data
    except requests.exceptions.Timeout:
        print("Error: API request timed out.")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to API. Check your internet.")
    except requests.exceptions.HTTPError:
        print("Error: Invalid city or API key.")
    except Exception as e:
        print("Unexpected Error:", str(e))
    return None
get_weather_with_errors("Hyderabad")
