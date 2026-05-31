import requests

api_key = "0e2ef70b298e59f3bf367ff73a02b3b8"

# while True:
def get_weather(city):

    # if city.lower() == 'exit':
    #     break

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:

            temperature = data["main"] ["temp"]
            humidity = data ["main"] ["humidity"]
            weather = data["weather"][0]["description"]

            print("\n----- WEATHER REPORT -----")
            print(f'City: {city}')
            print(f'Temperature: {temperature}')
            print(f'Humidity: {humidity}')
            print(f'Weather condition: {weather}')
            print("="*30)
            print('\n Thank you for using my weather app')
        else:
            print(f"Error {response.status_code}: {data.get('message', 'Unknown error')}")

    except Exception as e:
        print("An error occured")
        print(e)

city_name = input('Enter city name: ')
get_weather(city_name)
