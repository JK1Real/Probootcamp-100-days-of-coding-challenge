from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.keys import Keys


url = "https://en.wikipedia.org/wiki/Main_Page"

chromeOptions = ChromeOptions()
chromeOptions.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chromeOptions)
driver.get(url=url)
count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")

print(count.text)
# count.click()

portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# portals.click()

search =driver.find_element(By.NAME, value="search")
search.send_keys("python", Keys.ENTER)


# driver.quit()