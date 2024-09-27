from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from time import sleep
from selenium.webdriver.common.keys import Keys

url ="https://www.instagram.com/krishnaik06/"

user = "thisisnotallowed384@gmail.com"
password="merojloyaj"

chromeOptions=ChromeOptions()
chromeOptions.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chromeOptions)
driver.get(url=url)

sleep(5)
try:
    login = driver.find_element(by=By.LINK_TEXT, value='Log in')
    print(login.text)
    login.click()
except Exception as e:
    print(f"error {e}")

sleep(10)
email = driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
email.send_keys(user)
passwordlogin= driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
passwordlogin.send_keys(password)

next_login = driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button')
next_login.click()

sleep(10)

notnow = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div')
notnow.click()

sleep(10)
followers = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/header/section/div[3]/ul/li[2]/div/a')
followers.click()

followers_list = driver.find_elements(by=By.XPATH, value='/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div[2]')
for i in range(5):
    followers_list.send_keys(Keys.END)
    sleep(2)

# sleep(10)
# follows=driver.find_elements(by=By.XPATH, value="//buttton[contains(text(),'Follow')]")
# print(len(follows))
# follows[0].text
# follows[1].text

