from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep chromebrowser open after program finishes
chrome_option  = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option)
url = "https://www.python.org"
driver.get(url=url)

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text

# print(f"The price is {price_dollar}.{price_cents}")

search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.get_attribute("placeholder"))

button =driver.find_element(By.ID, value="submit")
print(button.size)

docs = driver.find_elements(By.CSS_SELECTOR, value=".main-footer .main-footer-links .container ul li.tier-1.element-3 ul li.tier-2.element-1 a")
print(docs[0].text)

documentations = driver.find_element(By.XPATH, value='//*[@id="container"]/li[3]/a')
print(documentations.text)

driver.quit()
# driver.close()
