from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions
from time import sleep
from selenium.common.exceptions import NoSuchWindowException 

chromeOptions = ChromeOptions()
chromeOptions.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chromeOptions)

url = "https://www.linkedin.com/jobs/search/?currentJobId=3769048860&f_AL=true&f_E=2&geoId=102713980&keywords=data%20scientist&location=India&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true"

email = "jeromk60@gmail.com"
password = "merojloyaj"

driver.get(url=url)

sleep(2)
signin = driver.find_element(by=By.XPATH, value='/html/body/div[1]/header/nav/div/a[2]')
signin.click()

sleep(5)

fill_email = driver.find_element(by=By.CSS_SELECTOR, value="#username")
fill_email.send_keys(email)

fill_password = driver.find_element(by=By.XPATH, value='//*[@id="password"]')
fill_password.send_keys(password)

sign = driver.find_element(by=By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')
sign.click()
a = input("enter")

easy_apply_button = driver.find_element(by=By.XPATH, value='//*[@id="ember48"]')
easy_apply_button.click()

all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")
print(len(all_listings))

company = driver.find_elements(by=By.CSS_SELECTOR, value="ul li a")

print(len(company))

# def first_next_button():
#     sleep(1)
#     first_next_button = driver.find_elements(by=By.CSS_SELECTOR, value='footer div button')
#     first_next_button[-1].click()

# first_next_button()
# first_next_button()
# first_next_button()
# first_next_button()
# first_next_button()


