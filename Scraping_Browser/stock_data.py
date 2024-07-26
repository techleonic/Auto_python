import requests
from datetime import datetime
import  time
ticker =  input("Enter the ticker:")
from_date = input("Enter start  date in yyy/mm/dd")
to_date = input("Enter start  date in yyy/mm/dd")

f = datetime.strptime(from_date,'%Y/%m/%d')
t = datetime.strptime(to_date, '%Y/%m/%d')
from_epoch = int(time.mktime(f.timetuple()))
to_epoch = int(time.mktime(t.timetuple()))

url = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={from_epoch}&period2={to_epoch}&interval=1d&events=history&includeAdjustedClose=true'
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}

#you can put .text for only text and open with write mode
#but if you use .content and open with wb mode you can save image eny binary file
content = requests.get(url,headers=headers).content

print(content)

with open("data.csv", "wb") as file:
    file.write(content)