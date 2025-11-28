import requests

def get_weather(city_name):
    api_key = 'd0d9c29cd5e0f6aa41e9370ad3874404'  # Your API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise error for bad responses

        data = response.json()

        # Extract required fields
        city = data['name']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']

        # Display in user-friendly format
        print(f"City: {city}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {description.capitalize()}")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Other error occurred: {err}")
    except KeyError:
        print("Error: Unexpected response format from API")

# Example usage
city_input = input("Enter city name: ")
get_weather(city_input)
