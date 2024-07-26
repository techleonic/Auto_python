from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from datetime import datetime
def save_file(text):
    try:
        with open("AverageTemp.txt","a") as file:
            file.write(text)
    except FileNotFoundError:
        with open("AverageTemp.txt","w") as file:
            file.write(text)


def get_driver():
    #set options
    options= webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument('disable-dev-shm-usage')
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    web="http://automated.pythonanywhere.com/login/"
    driver = webdriver.Chrome(options=options)
    driver.get(web)
    return driver

def clean_text(text):
    filter_text = text.split(": ")[1]
    return filter_text
def main():
    driver = get_driver()
    # element = driver.find_element(By.XPATH, "/html/body/div[1]/div/h1[1]")
    driver.find_element(By.ID, value="id_username").send_keys("automated")
    time.sleep(2)
    driver.find_element(By.ID, value="id_password").send_keys("automatedautomated"+Keys.RETURN)
    driver.find_element(By.XPATH, value="/html/body/nav/div/a").click()
    for _  in range(10):
        currentime = str(datetime.now())
        time.sleep(2)
        temp = driver.find_element(By.XPATH, value="/html/body/div[1]/div/h1[2]/div")
        text = clean_text(temp.text)
        save_file(f"{currentime} : {text}\n")


print(main())

