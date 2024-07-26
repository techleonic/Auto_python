from selenium import webdriver
from selenium.webdriver.common.by import By
import time
def get_driver():
    #set options
    options= webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument('disable-dev-shm-usage')
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    web="http://automated.pythonanywhere.com/"
    driver = webdriver.Chrome(options=options)
    driver.get(web)
    return driver

def main():
    driver = get_driver()
    time.sleep(2)
    # element = driver.find_element(By.XPATH, "/html/body/div[1]/div/h1[1]")
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/h1[2]')
    return element.text

print(main())