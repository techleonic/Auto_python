from selenium import webdriver
from selenium.webdriver.common.by import By
def get_driver():
    #set options
    options= webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument('disable-dev-shm-usage')
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    word = input("ENTER YOUR WORD TO EXPLAIN\n")
    web="https://dictionary.cambridge.org/es/diccionario/ingles-espanol/help"
    web = web.replace("help",word)
    driver = webdriver.Chrome(options=options)
    driver.get(web)
    return driver

def main():
    driver = get_driver()
    # element = driver.find_element(By.XPATH, "/html/body/div[1]/div/h1[1]")
    element = driver.find_element(By.XPATH, '//*[@id="dataset-caldes"]/div[2]/div[2]/div/span/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div')
    return element.text