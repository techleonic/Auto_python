import json
import requests

API_KEY = "e11054591b8c45ce8dfad2aa2452c278"
URL = "https://newsapi.org/v2/everything?q=apple&from=2024-07-27&to=2024-07-27&sortBy=popularity&language=en&apiKey=e11054591b8c45ce8dfad2aa2452c278"



def get_news(topic, from_date, to_date, languaje="en"):
    URL = f"https://newsapi.org/v2/everything?q={topic}&from={from_date}&to={to_date}&sortBy=popularity&language={languaje}&apiKey={API_KEY}"
    content = requests.get(URL).json()

    #remove null newss
    for news in content["articles"]:
        if news["content"] == "[Removed]":
           content["articles"].remove(news)

    #format  the json file
    content_format = json.dumps(content, indent=4)

    #write de json file
    with open("news.json", "w") as file:
        file.write(content_format)

    for news in content["articles"]:
        print(f"Title:{news["title"]}\nAutor:{news["author"]}\n\nc")


get_news("apple","2024-07-27","2024-07-27")
# print(content["articles"][0]["title"])