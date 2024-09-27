from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver import ChromeOptions


chromeOptions=ChromeOptions()
chromeOptions.add_experimental_option("detach", True)

signup_url = "http://secure-retreat-92358.herokuapp.com/"

driver = webdriver.Chrome(options=chromeOptions)
driver.get(url=signup_url)

fname = driver.find_element(By.NAME, value="fName")
fname.send_keys("aksjnd")

lname = driver.find_element(By.NAME, value="lName")
lname.send_keys("ksjbdkjs")

email = driver.find_element(By.NAME, value="email")
email.send_keys("daksnd@gmail.com")

submit = driver.find_element(By.TAG_NAME, value="button")
submit.send_keys(Keys.ENTER)

driver.quit()

