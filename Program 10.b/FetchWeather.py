import json
with open(#Enter path for the weather_data.json file
          r'weather_data.json') as f: 
    data = json.load(f)
curr_temp = data['main']['temp'] 
humidity = data['main']['humidity']
weather_desc = data['weather'][0]['description'] 
print(f"Current temperature: {curr_temp}°C")
print(f"Humidity: {humidity}%") 
print(f"Weather description: {weather_desc}")