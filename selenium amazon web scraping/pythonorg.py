from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By


url = "https://www.python.org/"


chrome_option = ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option)
driver.get(url=url)

dates = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
values = dates[0].text


texts = values.split("\n")


dictionary = {int(text/2):{'time':texts[text],'name':texts[text+1]} for text in range(0, len(texts), 2) }

print(dictionary)
driver.quit ()
