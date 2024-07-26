from bs4 import BeautifulSoup
import requests
def get_currency(in_currency, out_curency):
    url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_curency}&amount=1"
    content= requests.get(url).text
    soup = BeautifulSoup(content,'html.parser')
    rate = soup.find("span",class_="ccOutputRslt").getText()
    rate = float(rate[0:7])
    return (rate)

print(get_currency("USD","CNY"))