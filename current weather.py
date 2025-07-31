import requests

API_KEY = 'b0bbc748c6b94d4ea5051601252107'  # Replace with your WeatherAPI key
CITY = 'Hyderabad'             # You can change this to any city

url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}&aqi=no"

response = requests.get(url)
data = response.json()

#print(data)

if response.status_code == 200:
    location = data['location']['name']
    region = data['location']['region']
    country = data['location']['country']
    temp_c = data['current']['temp_f']
    condition = data['current']['condition']['text']
    print(f"Weather in {location}, {region}, {country}:")
    print(f"Temperature: {temp_c} °F")
    print(f"condition : {condition}")
    
else:
    print("Error:", data.get("error", {}).get("message", "Something went wrong."))
