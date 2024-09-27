from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions
from selenium import webdriver
from time import sleep

chromeOptions=ChromeOptions()
chromeOptions.add_experimental_option("detach", True)

url = "https://www.thispersondoesnotexist.com/"

driver = webdriver.Chrome(options=chromeOptions)
driver.get(url=url)

sleep(10)
for i in range(0, 10):
    sleep(3)
    driver.refresh()

