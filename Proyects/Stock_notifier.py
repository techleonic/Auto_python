
from selenium import webdriver
from    selenium.webdriver.common.by import By
from time import sleep
import yagmail
import os
def get_driver(web):
    #set options
    options= webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument('disable-dev-shm-usage')
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)
    driver.get(web)
    return driver
def send_mail(stock, trend):
    sender = os.getenv("SENDER_EMAIL")
    receiver = os.environ.get("RECIVER_EMAIL")

    subject = f"Subject: Stock Price is {trend}"

    content = f"""\
    stock price is {stock}
    """
    print(content)
    yag = yagmail.SMTP(user=sender, password=os.getenv("SENDER_PASSWORD"))
    yag.send(to=receiver, subject=subject, contents=content)

if __name__ == '__main__':
    driver = get_driver("https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6&ta")
    sleep(2)
    stock_value = driver.find_element(By.XPATH, '//*[@id="app_indeks"]/section[1]/div/div/div[2]/span[2]')
    stock_trend = driver.find_element(By.XPATH, '//*[@id="app_indeks"]/section[1]/div/div/div[2]/span[1]')
    send_mail(stock_value.text,stock_trend.text)