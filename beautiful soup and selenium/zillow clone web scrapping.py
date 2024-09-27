import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

zillow_clone_url = "https://appbrewery.github.io/Zillow-Clone/"
form_url = "https://docs.google.com/forms/d/e/1FAIpQLSf8WX-n3rs0bQ1OmIQSDNyB0P2nqNP0rTaz7EKBwpQCap6BkA/viewform?usp=sf_link"


respone = requests.get(url=zillow_clone_url)
contents = respone.content

soup = BeautifulSoup(contents,'html.parser')
list = soup.find_all('li')
print(len(list))
rent_amount=[]
address=[]
links=[]
for i in list:
    try:
        price = i.find("span", class_="PropertyCardWrapper__StyledPriceLine")
        add=i.find("address")
        link=i.find("a")
        if "+" in price.text: 
            print(price.text.split("+")[0])
        else:
            print(price.text.split("/")[0])
        print(add.text.strip())
        print(link.get("href"))
        links.append(link.get("href"))
        if "+" in price.text: 
            rent_amount.append(price.text.split("+")[0])
        else:
            rent_amount.append(price.text.split("/")[0])

        address.append(add.text.strip().replace("|",""))
    except:
        pass
    

chromeOptions = ChromeOptions()
chromeOptions.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chromeOptions)

driver.get(url=form_url)


for add, rent, link in zip(address, rent_amount, links):
    sleep(3)
    address_of_the_property = driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_of_the_property.send_keys(add)

    price_per_month =driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_per_month.send_keys(rent)

    link_to_the_property = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_to_the_property.send_keys(link)

    submit = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    submit.click()

    sleep(2)
    submit_another_response=driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    submit_another_response.click()

