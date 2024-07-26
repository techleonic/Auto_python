from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
def get_driver():
    #set options
    options= webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument('disable-dev-shm-usage')
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    web="https://titan22.com/account/login/"
    driver = webdriver.Chrome(options=options)
    driver.get(web)
    return driver

def main():
    driver = get_driver()
    # element = driver.find_element(By.XPATH, "/html/body/div[1]/div/h1[1]")
    driver.find_element(By.ID, value="CustomerEmail").send_keys("lzq08591@tccho.com")
    time.sleep(2)
    driver.find_element(By.ID, value="CustomerPassword").send_keys("1234567"+Keys.RETURN)
    time.sleep(2)
    driver.find_element(By.XPATH, value="/html/body/footer/div/section/div/div[1]/div[1]/div[1]/nav/ul/li[1]/a").click()
    time.sleep(2)
    return driver.current_url

print(main())