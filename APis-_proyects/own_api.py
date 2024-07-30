from flask import Flask,jsonify
from bs4 import BeautifulSoup
import requests
def get_currency(in_currency, out_curency):
    url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_curency}&amount=1"
    content= requests.get(url).text
    soup = BeautifulSoup(content,'html.parser')
    rate = soup.find("span",class_="ccOutputRslt").getText()
    rate = float(rate[0:7])
    return (rate)


app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Currency Rate Api </h1> <p> Example URL:/api/v1/usd-eur</p> '

@app.route('/api/v1/<in_cur>-<out_cur>')
def api(in_cur,out_cur):
    rate = get_currency(in_cur,out_cur)
    result_dict = {"input_currency":in_cur, "output_currency":out_cur, "rate":rate}
    return jsonify(result_dict)
app.run()