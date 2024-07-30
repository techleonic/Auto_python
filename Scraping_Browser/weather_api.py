import requests
lat = 12.62
lon = -87.12
API_KEY = ""
# content =  requests.get(url).json()

def get_weather(city, units = "metric",apikey = API_KEY):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={apikey}&units={units}"
    r = requests.get(url)
    content = r.json()
    with open("data.txt","a") as file:
        for item in content["list"]:
           file.write(f'\n{city},{item["dt_txt"]},{item["dt_txt"],item["main"]["temp"]},{item["weather"][0]["description"]}')

print(get_weather(city="Managua"))