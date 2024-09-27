from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
# Twitter login link
speed_tester_url = "https://www.speedtest.net/result/16292333944"




chromeOptions = ChromeOptions()
chromeOptions.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chromeOptions)

driver.get(url=speed_tester_url)
a=input("enter")
sleep(10)
continu = driver.find_element(by=By.ID, value='onetrust-accept-btn-handler')
continu.click()

speed = driver.find_elements(by=By.CSS_SELECTOR, value='.start-button a')
print(len(speed))
print(f"The element is {speed}")
print(speed[0].text)
try:
    print(speed[0].click())
except Exception as e:
    print(f"exception is {e}")


sleep(10)
download_speed = driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
download_speed = download_speed.text


upload_speed = driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
upload_speed = upload_speed.text

print(f"download speed is {download_speed}, upload speed is {upload_speed}")

driver.quit()


