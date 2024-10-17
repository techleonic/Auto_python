import requests
from bs4 import BeautifulSoup

response = requests.get(url='https://filesamples.com/formats/mp3')
soup =  BeautifulSoup(response.text, "html.parser")

anchors =  soup.find_all(name='a', attrs={'download':"",'class':"btn btn-blue col-span-3 md:col-span-1"})
links = []
for anchor in anchors:
    print(anchor)
    f_anchor = anchor.get('href').replace(" ", "%")
    link= 'https://filesamples.com/'+f_anchor
    links.append(link)

for mp3_link in links:
    try:
        req = requests.get(mp3_link)
        with open(f'{links.index(mp3_link)}.mp3', 'wb') as file:
            file.write(req.content)
    except:
        pass

