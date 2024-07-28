import json

import requests

API_KEY = "e11054591b8c45ce8dfad2aa2452c278"
URL = "https://newsapi.org/v2/everything?q=apple&from=2024-07-27&to=2024-07-27&sortBy=popularity&language=en&apiKey=e11054591b8c45ce8dfad2aa2452c278"
content = requests.get(URL).json()

content_format = json.dumps(content, indent=4)

with open("news.json","w") as file:
    file.write(content_format)

for articles in content["articles"]:
    print(articles["title"])
# print(content["articles"][0]["title"])