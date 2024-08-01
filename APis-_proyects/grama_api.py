import requests
import json
url = "https://api.languagetool.org/v2/check"
data = {"text":"tis is nixe day","language":"auto"}
response = requests.post(url,data=data)
result = json.loads(response.text)
print(response.text)